for f in *.pdf ; do
  pdftk "$f" output "../$f" user_pw p4ssw0rd allow printing
done
