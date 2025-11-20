#!/bin/bash
set -e

VERSION="3.1.0"
DMG_FILE="Release/SuperBirdID-v${VERSION}.dmg"
DEVELOPER_ID="Developer ID Application: James Zhen Yu (JWR6FDB52H)"
KEYCHAIN_PROFILE="AC_PASSWORD"

echo "🔐 SuperBirdID v${VERSION} 签名和公证流程"
echo "============================================"

# 检查 DMG 文件是否存在
if [ ! -f "$DMG_FILE" ]; then
    echo "❌ 错误: 未找到 DMG 文件: $DMG_FILE"
    exit 1
fi

# 1. 签名 DMG
echo ""
echo "📝 步骤 1: 签名 DMG..."
codesign --sign "$DEVELOPER_ID" "$DMG_FILE"
echo "✅ DMG 签名完成"

# 2. 验证签名
echo ""
echo "🔍 步骤 2: 验证签名..."
codesign -vvv "$DMG_FILE"
echo "✅ 签名验证通过"

# 3. 提交公证
echo ""
echo "📤 步骤 3: 提交公证（这可能需要几分钟）..."
echo "如果看到 401 错误，请先设置 notarytool 凭据："
echo "  xcrun notarytool store-credentials \"$KEYCHAIN_PROFILE\" \\"
echo "    --apple-id <your-apple-id> \\"
echo "    --team-id JWR6FDB52H \\"
echo "    --password <app-specific-password>"
echo ""

# 提交公证并等待
SUBMIT_OUTPUT=$(xcrun notarytool submit "$DMG_FILE" \
    --keychain-profile "$KEYCHAIN_PROFILE" \
    --wait 2>&1)

echo "$SUBMIT_OUTPUT"

# 检查是否成功
if echo "$SUBMIT_OUTPUT" | grep -q "Invalid credentials"; then
    echo ""
    echo "❌ 公证失败: 凭据无效"
    echo ""
    echo "请按以下步骤设置凭据："
    echo "1. 访问 https://appleid.apple.com"
    echo "2. 登录您的 Apple ID"
    echo "3. 在\"安全\"部分，生成一个应用专用密码"
    echo "4. 运行以下命令保存凭据："
    echo ""
    echo "   xcrun notarytool store-credentials \"$KEYCHAIN_PROFILE\" \\"
    echo "     --apple-id <your-apple-id> \\"
    echo "     --team-id JWR6FDB52H \\"
    echo "     --password <app-specific-password>"
    echo ""
    exit 1
fi

if echo "$SUBMIT_OUTPUT" | grep -q "status: Accepted"; then
    echo "✅ 公证成功"

    # 4. 装订公证票据
    echo ""
    echo "📎 步骤 4: 装订公证票据..."
    xcrun stapler staple "$DMG_FILE"
    echo "✅ 票据装订完成"

    # 5. 验证装订
    echo ""
    echo "🔍 步骤 5: 验证装订..."
    xcrun stapler validate "$DMG_FILE"
    echo "✅ 装订验证通过"

    # 6. 验证 Gatekeeper
    echo ""
    echo "🔍 步骤 6: 验证 Gatekeeper..."
    spctl -a -t open --context context:primary-signature -v "$DMG_FILE"
    echo "✅ Gatekeeper 验证通过"

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🎉 签名、公证和装订全部完成！"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📦 已签名并公证的 DMG:"
    ls -lh "$DMG_FILE"
    echo ""
    echo "SHA256:"
    shasum -a 256 "$DMG_FILE"
    echo ""
    echo "✅ 文件已准备好发布！"

else
    echo ""
    echo "❌ 公证失败"
    echo ""
    echo "请检查输出中的错误信息"

    # 尝试提取提交 ID 并显示日志
    SUBMISSION_ID=$(echo "$SUBMIT_OUTPUT" | grep "id:" | head -1 | awk '{print $2}')
    if [ ! -z "$SUBMISSION_ID" ]; then
        echo ""
        echo "提交 ID: $SUBMISSION_ID"
        echo "查看详细日志："
        echo "  xcrun notarytool log $SUBMISSION_ID --keychain-profile \"$KEYCHAIN_PROFILE\""
    fi

    exit 1
fi
