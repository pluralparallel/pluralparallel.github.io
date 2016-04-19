ls
echo $PWD
git checkout source
git clone https://github.com/onur/medius.git
pelican-themes -i medius/
pelican content
git config --local user.name pluralparallel
git config --local user.email pluralparallel@circleci.com
git checkout master
git reset --hard 7ed15ee136
git push origin master --force
mv output /tmp
mv LICENSE /tmp
rm -rf *
mv /tmp/LICENSE .
cp -rf /tmp/output/* .
git add --all
git commit -m 'Update documentation'
git push origin master
