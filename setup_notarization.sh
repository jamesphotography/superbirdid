#!/bin/bash

echo "🔐 设置 Apple 公证凭据"
echo "================================"
echo ""
echo "在继续之前，您需要："
echo "1. Apple ID（通常是您的 @icloud.com 邮箱）"
echo "2. Team ID: JWR6FDB52H"
echo "3. 应用专用密码（App-Specific Password）"
echo ""
echo "如果还没有应用专用密码，请按以下步骤获取："
echo "1. 访问 https://appleid.apple.com"
echo "2. 登录您的 Apple ID"
echo "3. 在\"安全\"部分，点击\"应用专用密码\""
echo "4. 点击\"生成密码\""
echo "5. 输入标签（例如：SuperBirdID Notarization）"
echo "6. 复制生成的密码（格式：xxxx-xxxx-xxxx-xxxx）"
echo ""
echo "按回车键继续，或按 Ctrl+C 取消..."
read

echo ""
echo "请输入您的 Apple ID:"
read APPLE_ID

echo ""
echo "请输入应用专用密码（粘贴后不会显示）:"
read -s APP_PASSWORD

echo ""
echo ""
echo "正在保存凭据到钥匙串..."

xcrun notarytool store-credentials "AC_PASSWORD" \
    --apple-id "$APPLE_ID" \
    --team-id "JWR6FDB52H" \
    --password "$APP_PASSWORD"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 凭据保存成功！"
    echo ""
    echo "测试凭据..."
    xcrun notarytool history --keychain-profile "AC_PASSWORD" 2>&1 | head -5

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ 凭据验证成功！"
        echo ""
        echo "现在可以运行签名和公证脚本："
        echo "  ./sign_and_notarize_v3.1.0.sh"
    else
        echo ""
        echo "⚠️ 凭据保存成功，但验证失败"
        echo "请检查 Apple ID 和密码是否正确"
    fi
else
    echo ""
    echo "❌ 凭据保存失败"
    echo "请检查输入的信息是否正确"
fi
