{
svn checkout https://github.com/TiriAI/TiOS/trunk/TiriUI &&
mv -v TiriUI/* TiOS &&
rm -r TiriUI &&
cd TiOS &&
rm -r raspbian &&
} || {
  echo "WiFi Not Connected, updates not available"
}
