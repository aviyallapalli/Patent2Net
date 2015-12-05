rmdir /S /Q dist\Patent2Net

pyinstaller -y --noupx --specpath=specs --clean  --version-file=version-FormateExportAttractivityCartography.txt FormateExportAttractivityCartography.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-OPSGatherPatentsv2.txt OPSGatherPatentsv2.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-OPSGatherContentsv2-Iramuteq.txt OPSGatherContentsv2-Iramuteq.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-OPSGatherAugment-Families.txt OPSGatherAugment-Families.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-networksMix.txt  P2N-networksMix.py
REM pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-networksCit.txt P2N-networksCit.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksRefs.txt P2N-NetworksRefs.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-PreNetworksRefs.txt P2N-PreNetworksRefs.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksRefsJS.txt P2N-NetworksRefsJS.py

pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksEquiv.txt P2N-NetworksEquiv.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-PreNetworksEquiv.txt P2N-PreNetworksEquiv.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksEquivJS.txt P2N-NetworksEquivJS.py

pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksCitations.txt P2N-NetworksCitations.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-PreNetworksCitations.txt P2N-PreNetworksCitations.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-NetworksCitationsJS.txt P2N-NetworksCitationsJS.py

pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FusionIramuteq2.txt FusionIramuteq2.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-Fusion.txt Fusion.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-P2N-FreePlane.txt P2N-FreePlane.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FormateExportDataTable.txt FormateExportDataTable.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FormateExportPivotTable.txt FormateExportPivotTable.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FormateExportDataTableFamilies.txt FormateExportDataTableFamilies.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FormateExportBiblio.txt FormateExportBiblio.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FormateExportCountryCartography.txt FormateExportCountryCartography.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-FusionCarrot2.txt FusionCarrot2.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-Interface2.txt Interface2.py
pyinstaller -y --noupx --specpath=specs --clean --version-file=version-Parallel2.txt Parallel2.py

pyinstaller -y --noupx --version-file=version-FormateExportAttractivityCartography.txt specs\FormateExportAttractivityCartography.spec
pyinstaller -y --noupx --version-file=version-OPSGatherPatentsv2.txt specs\OPSGatherPatentsv2.spec
pyinstaller -y --noupx --version-file=version-OPSGatherContentsv2-Iramuteq.txt specs\OPSGatherContentsv2-Iramuteq.spec
pyinstaller -y --noupx --version-file=version-OPSGatherAugment-Families.txt specs\OPSGatherAugment-Families.spec
pyinstaller -y --noupx --version-file=version-P2N-networksMix.txt specs\P2N-networksMix.spec
REM pyinstaller -y --noupx --version-file=version-P2N-networksCit.txt specs\P2N-networksCit.spec
pyinstaller -y --noupx --version-file=version-P2N-NetworksRefs.txt specs\P2N-NetworksRefs.spec
pyinstaller -y --noupx --version-file=version-P2N-PreNetworksRefs.txt specs\P2N-PreNetworksRefs.spec
pyinstaller -y --noupx --version-file=version-P2N-NetworksRefsJS.txt specs\P2N-NetworksRefsJS.spec

pyinstaller -y --noupx --version-file=version-P2N-NetworksEquiv.txt specs\P2N-NetworksEquiv.spec
pyinstaller -y --noupx --version-file=version-P2N-PreNetworksEquiv.txt specs\P2N-PreNetworksEquiv.spec
pyinstaller -y --noupx --version-file=version-P2N-NetworksEquivJS.txt specs\P2N-NetworksEquivJS.spec

pyinstaller -y --noupx --version-file=version-P2N-NetworksCitations.txt specs\P2N-NetworksCitations.spec
pyinstaller -y --noupx --version-file=version-P2N-PreNetworksCitations.txt specs\P2N-PreNetworksCitations.spec
pyinstaller -y --noupx --version-file=version-P2N-NetworksCitationsJS.txt specs\P2N-NetworksCitationsJS.spec

pyinstaller -y --noupx --version-file=version-FusionIramuteq2.txt specs\FusionIramuteq2.spec
pyinstaller -y --noupx --version-file=version-Fusion.txt specs\Fusion.spec
pyinstaller -y --noupx --version-file=version-P2N-FreePlane.txt specs\P2N-FreePlane.spec
pyinstaller -y --noupx --version-file=version-FormateExportDataTable.txt specs\FormateExportDataTable.spec
pyinstaller -y --noupx --version-file=version-FormateExportPivotTable.txt specs\FormateExportPivotTable.spec
pyinstaller -y --noupx --version-file=version-FormateExportDataTableFamilies.txt specs\FormateExportDataTableFamilies.spec
pyinstaller -y --noupx --version-file=version-FormateExportBiblio.txt specs\FormateExportBiblio.spec
pyinstaller -y --noupx --version-file=version-FormateExportCountryCartography.txt specs\FormateExportCountryCartography.spec
pyinstaller -y --noupx --version-file=version-FusionCarrot2.txt specs\FusionCarrot2.spec
pyinstaller -y --noupx --version-file=version-Interface2.txt specs\Interface2.spec
pyinstaller -y --noupx --version-file=version-Parallel2.txt specs\Parallel2.spec

mkdir dist\Patent2Net\

xcopy /S /Y dist\FormateExportAttractivityCartography dist\Patent2Net\ 
xcopy /S /Y dist\OPSGatherPatentsv2 dist\Patent2Net\ 
xcopy /S /Y dist\OPSGatherContentsv2-Iramuteq dist\Patent2Net\
xcopy /S /Y dist\OPSGatherAugment-Families dist\Patent2Net\
xcopy /S /Y dist\P2N-NetworksMix dist\Patent2Net\
REM xcopy /S /Y dist\P2N-NetworksCit dist\Patent2Net\
xcopy /S /Y dist\P2N-NetworksRefs dist\Patent2Net\
xcopy /S /Y dist\P2N-PreNetworksRefs dist\Patent2Net\
xcopy /S /Y dist\P2N-NetworksRefsJS dist\Patent2Net\

xcopy /S /Y dist\P2N-NetworksEquiv dist\Patent2Net\
xcopy /S /Y dist\P2N-PreNetworksEquiv dist\Patent2Net\
xcopy /S /Y dist\P2N-NetworksEquivJS dist\Patent2Net\

xcopy /S /Y dist\P2N-NetworksCitations dist\Patent2Net\
xcopy /S /Y dist\P2N-PreNetworksCitations dist\Patent2Net\
xcopy /S /Y dist\P2N-NetworksCitationsJS dist\Patent2Net\

xcopy /S /Y dist\FusionIramuteq2 dist\Patent2Net\
xcopy /S /Y dist\Fusion dist\Patent2Net\
xcopy /S /Y dist\P2N-FreePlane dist\Patent2Net\
xcopy /S /Y dist\FormateExportDataTable dist\Patent2Net\
xcopy /S /Y dist\FormateExportPivotTable dist\Patent2Net\
xcopy /S /Y dist\FormateExportDataTableFamilies dist\Patent2Net\
xcopy /S /Y dist\FormateExportBiblio dist\Patent2Net\
xcopy /S /Y dist\FormateExportCountryCartography dist\Patent2Net\
xcopy /S /Y dist\FusionCarrot2 dist\Patent2Net\
xcopy /S /Y dist\Interface2 dist\Patent2Net\
xcopy /S /Y dist\Parallel2 dist\Patent2Net\



rmdir /S /Q dist\FormateExportAttractivityCartography
rmdir /S /Q dist\OPSGatherPatentsv2
rmdir /S /Q dist\OPSGatherContentsv2-Iramuteq
rmdir /S /Q dist\OPSGatherAugment-Families
rmdir /S /Q dist\P2N-NetworksMix
REM rmdir /S /Q dist\P2N-NetworksCit
rmdir /S /Q  dist\P2N-NetworksRefs
rmdir /S /Q  dist\P2N-PreNetworksRefs
rmdir /S /Q  dist\P2N-NetworksRefsJS

rmdir /S /Q  dist\P2N-NetworksEquiv
rmdir /S /Q  dist\P2N-PreNetworksEquiv
rmdir /S /Q  dist\P2N-NetworksEquivJS

rmdir /S /Q  dist\P2N-NetworksCitations
rmdir /S /Q  dist\P2N-PreNetworksCitations
rmdir /S /Q  dist\P2N-NetworksCitationsJS

rmdir /S /Q dist\FusionIramuteq2
rmdir /S /Q dist\Fusion
rmdir /S /Q dist\P2N-FreePlane
rmdir /S /Q dist\FormateExportDataTable
rmdir /S /Q dist\FormateExportPivotTable
rmdir /S /Q dist\FormateExportDataTableFamilies
rmdir /S /Q dist\FormateExportBiblio
rmdir /S /Q dist\FormateExportCountryCartography
rmdir /S /Q dist\FusionCarrot2 
rmdir /S /Q dist\Interface2
rmdir /S /Q dist\Parallel2



REM xcopy /S /Y dist\P2N-FamiliesHierarc dist\Patent2Net\

xcopy /Y root\* dist\

copy /Y requete.cql dist
copy /y cacert.pem dist\Patent2Net\
copy /y countries.json dist\patent2Net
copy /y P2N.css dist\patent2Net
copy /y ModeleCarto.html dist\patent2Net
copy /y ModeleCartoDeposant.html dist\patent2Net
copy /y NameCountryMap.csv dist\Patent2Net\
copy /y scriptSearch.js dist\Patent2Net\
copy /y Searchscript.js dist\Patent2Net\
copy /y config.js dist\Patent2Net\
copy /y CollecteETRaite.bat dist
copy /y Modele.html dist\Patent2Net\Modele.html
copy /y Graphe.html dist\Patent2Net\Graphe.html
copy /y OpenNav.bat dist\Patent2Net\OpenNav.bat
copy /y ModeleFamille.html dist\Patent2Net\ModeleFamille.html
copy /y ModeleFamillePivot.html dist\Patent2Net\ModeleFamillePivot.html
copy /y Pivot.html dist\Patent2Net\Pivot.html
copy /y ModeleIndex.html dist\Patent2Net\ModeleIndex.html
copy /y ModeleContenuIndex.html dist\Patent2Net\ModeleContenuIndex.html
copy /y ModeleIndexRequete.html dist\Patent2Net\
copy /y cles-epo.txt dist
mkdir dist\Patent2Net\lib2to3
xcopy /S /Y lib2to3 dist\Patent2Net\lib2to3
mkdir dist\Patent2Net\extensions
mkdir dist\Patent2Net\media
xcopy /S /Y extensions dist\Patent2Net\extensions
xcopy /S /Y media dist\Patent2Net\media
