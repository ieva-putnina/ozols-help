
Aleksandrs 02.07.2020:-------------------------
Direktorija ar programmam:
  ozols-help/rst_creation
Galvena programma:
  ozols-help/rst_creation/index_rst.py
Programma kas parveido HTML kodu RST formatā:
  ozols-help/rst_creation/html2rest.py
Lai programma html2rest.py strādā python versija 3.8 jāinstalē bibliotēku sgmllib3k:
  pip3 install sgmllib3k
Izveidoti ar programmu index_rst.py RST faila glabājas direktorijā:
  ozols-help/rst_creation/rst_files
Izviedotus RST failus jākopē direktorijā ozols-help/source, kur atrodas konfiguracijas fails conf.py un shellscript build.sh, kuru jāizmanto lai izveidot sphinx vietni ar komandu:
  bash build.sh ~/doc-dev/ozols-help/source/ ~/doc-dev/ozols-help/build/html conf.py


Ieva 24.08.2020:------------------------
Lai atvērtu instrukciju ar pielāgoto CSS, interneta pārlūkā jāatver fails ozols-help/build/html/index.html.
Lai iedarbinātu failos ieviestās izmaiņas, termināli, esot lokācijā /opt/doc/ozols/ozols-help jāpalaiž darbība 'build html'.
Izmaiņas veiktas gan failā ozols-help/source/conf.py, gan mapē ozols-help/source/static, gan tēmas mapes ozols-help/source/_themes/sphinx_ozols_help_theme failos.
Galvenās izmaiņas var ieviest, pārrakstot failu ozols-help/source/_themes/sphinx_ozols_help_theme/glpi/static/glpi.css 
  (iznāk papildināt/pārveidot glpi tēmas CSS failu , kurš, savukārt, ir paredzēts local_rtd_theme theme.css faila mantošanai un pārrakstīšanai).
Pēc ikvienu izmaiņu ieviešanas, jāizdara 'build html' darbība, lai izmaiņas tiktu atspoguļotas.

