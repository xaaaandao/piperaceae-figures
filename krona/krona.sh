sudo apt-get update 
sudo apt-get install -y apache2 git git-core
/etc/init.d/apache2 start
git clone https://github.com/marbl/Krona.git
cd Krona/KronaTools/scripts/ && mv test.txt ~/Krona/KronaTools/scripts/ && ./scripts/ImportText.pl test.txt -o a.html && sudo cp a.html /var/www/html/index.html
