for f in *.pdf ; do
  pdftk "$f" output "pwd_$f" user_pw p4ssw0rd allow printing
done
