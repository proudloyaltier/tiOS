svn checkout https://github.com/TiriAI/TiOS/trunk/TiriUI
mv -v TiriUI/* TiOS
rm -r TiriUI
cd TiOS
chmod u+x TiriUI.py
rm -r raspbian
