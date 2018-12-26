svn checkout https://github.com/TiriAI/TiOS/trunk/TiriUI
mv -v TiriUI/* TiOS
rm -r TiriUI
cd TiOS
sudo chmod u+x TiriUI.py
sudo chown pi TiriUI.py
rm -r raspbian
