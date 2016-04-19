ls
echo $PWD
pelican-themes -i themes/medius/
pelican content -o /tmp/output
git config --local user.name pluralparallel
git config --local user.email pluralparallel@circleci.com
git checkout master
git reset --hard 7ed15ee136
git push origin master --force
mv LICENSE /tmp
rm -rf *
mv /tmp/LICENSE .
cp -rf /tmp/output/* .
git add --all
git commit -m 'Update documentation'
git push origin master
