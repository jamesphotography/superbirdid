#!/bin/bash
set -e

APP_PATH="dist/SuperBirdID.app"
DEVELOPER_ID="Developer ID Application: James Zhen Yu (JWR6FDB52H)"

echo "🔧 递归签名 app bundle 中的所有文件..."
echo ""

# 签名所有 .so 和 .dylib 文件
echo "📝 签名所有 .so 文件..."
find "${APP_PATH}" -name "*.so" -type f | while read file; do
    echo "  签名: $(basename "$file")"
    codesign --force --sign "${DEVELOPER_ID}" --timestamp --options runtime "$file" 2>/dev/null || true
done

echo ""
echo "📝 签名所有 .dylib 文件..."
find "${APP_PATH}" -name "*.dylib" -type f | while read file; do
    echo "  签名: $(basename "$file")"
    codesign --force --sign "${DEVELOPER_ID}" --timestamp --options runtime "$file" 2>/dev/null || true
done

echo ""
echo "📝 签名 Frameworks..."
find "${APP_PATH}/Contents/Frameworks" -type f -perm +111 | while read file; do
    if file "$file" | grep -q "Mach-O"; then
        echo "  签名: $(basename "$file")"
        codesign --force --sign "${DEVELOPER_ID}" --timestamp --options runtime "$file" 2>/dev/null || true
    fi
done

echo ""
echo "📝 签名主应用 bundle..."
codesign --force --sign "${DEVELOPER_ID}" --timestamp --options runtime \
  --entitlements /dev/null \
  "${APP_PATH}"

echo ""
echo "✅ App bundle 签名完成！"
