######################################################################
# Author: Elaheh Jamali
# Username: Jamalie

# Assignment: A4: Breaking Bad Ciphers
#
# Purpose: This assignment explores the process for cracking different ciphers.
#
# Acknowledgement: Dr. Maiti and Evan Johnson for helping to find a way to crack the bigger cipher
#
######################################################################
import math
big_cipher ="coovhsrerotovoaaaowednphrtyadertfeeikwualstratflknfsfrlrilsnwpjyhefwuereowonknhteu" \
       "tliwafitiysoriowohbdsspegbiaallhafmtieiaiaudtdouooelhnssrrurniateaddelrnkitindkoelw" \
       "euieasierplnrloiekoaiemlininmhrurrudlittnymrogsbenlmidtaeinnriiekaenegsrihbeeaoeokono" \
       "errddeeneldeaolsqyiishooiianwelniordlanrnioendetsdiwhpesulkruowuokewmykobtsatfeitmduuorn" \
       "wemthnggieetfvpoykdnuttdghphotteiafifebisdenwibnuoenrhonoorttebeiueehmeradowtobeherweewope" \
       "aafeienhwetrteftegeyldnfoesudtaiudtrswhoemtvcviirevtfihnirelanlsannllnofnlteomeroslhhhmrlyey" \
       "lrtmchistfhttaiwnyeetetgesehrtierisylelptooyfdraoihrursofieiitreperotiaroanitoehasnnolagorehnpa" \
       "aohtadnrfiroacnraastlnbaelpbtlsdsnoppaanuoscpmvssoucanigetigorwlttoctmiontterniprhowdnhhlietpdr" \
       "liimoidurluhngnphrpeui1natdptrlnrtaaayenomttwdhoseenoreeeehaeftriahaesfefsttaasanoeuealtrr5dmmtshyoeet" \
       "nnbrrdlyhmnieitsnelossgnogflsttualenetfaholcelnthtniaogr0merhwaeboeodtcismdliremntihovltisiougjabyhsvi" \
       "doeainefieoloovtonideelyrpiitaifqgceovariasprloincheyottaureotaoaeenimrbsecpnmwrtmeiienoolisarstshtiuoad" \
       "aeppwdvrnortiuertupungadrocfdonenoeomxoaeeniryrntgttnenetaicptdnidmttreriieaoowsltdnetlnbhgodnkebwuvdrslo" \
       "purpnegebygsoshivelhlshehoqtoeotstaswrlnkesltiesounlooushrxenzoeetiranrrtrharwoiemioasfeibolanueardooslhi" \
       "yioigtwldvtfmeufytmieaeezomhsctrtoaiqtloenpsrsnnydpnowlttianaorfhitsbnenioaeneitmdetofrsmmnrlmieiparetysusltl" \
       "astpjltoeeelnsswrgomtebonohoesgankftrnhemshuopbaiswemshnrlorsdiiuyhlfworoyiuptitetioyrtehvrpemtuiuaneeitdgetrs" \
       "ialrarniedaeapoctsmotermetaitabdskosnorhtraehnieimeaotlhtbdhshitctptsslackitlutdsecoporeoterrhlthlyonnshtniemkn" \
       "eelsatrlkcilholeihadeaorutsolkantlpeocaeiarpswlapsesceiottoiohotsroytreilipleoqtenuamftasgtanhuwitbgiottwecslurr" \
       "inylrpcehtnuhiwtpawwapwlosanasroamueseeduowntehlearinhltncohnaesrsyatedtaeummrekitmemtnamrnookvtchamcpelrriopra" \
       "yiaeiateneeehgotiesieuesltryeltsorainsardaceseaenseihhcliololeidwsystnnfnspdgpmbaouhsrefsnoqianoristupiwojtphnar" \
       "ablrgitneeoismawysgnnhoyhgdleiamaioitnrobndyadwunlnunnhosrniwotressspaiwelcgfclnspinothieouoittoslrepnmrpissiot" \
       "oroniekodaeomtassmbearbetucnerlhtikueolneuittruiunehotyrtriedateernouewerioiytwpealthrbnleriinkelaynhremewaarw" \
       "nnantfhgsurumohonnirsibdobhnnreswgoeeirciatpediioslmwilsfoesrblnibohgoyoiyimtmmnatalftdrptaweeaotwienuuelnlhn" \
       "torcannthlratwiawoteilenohamwbnnotriprnjitooinoewrosedwheveeewnlbeeeicaaneihawprshtrcwpdaortuytroeogutpnspeos" \
       "inrgitrasupsnieleirsadioamloolutwpelirdnahtonlswiwotespwanasirgirdrdtgtotwcsblietsclhsnsnitlvronmisyesrltaso" \
       "tiomeahiwhwtswrnuothnattaomesehtshhnednxntuiaenntnstepohpneelwwrhlatdnoercitianhtraetntogleslwrftdeiqeiannip" \
       "aorddenotghosrkeleialiaetisaoksoaerhsteiholriohwtishinpiosfmunnittniirtbaintomantaiaailhitsthnfpytinlitmhdrs" \
       "eninfneohntenerntqjhiitlevgrlyaelgogcrrhhlndibiwwclueeoaohlhowaytowpugnouocweeiaeraiauoorghemomeeeitoeteopdee" \
       "igdnekeihyrfprluilenanboyeahwenlnancyndnyltlarmeoedaorddsntotrtmrllcnarbgelsainaawiwsywenderorrtilopogeaegooei" \
       "elwdeltftpmpaioaekteseaylueteryblhtntkuanaitaotsseuerhtohleergltnwanlaksooiihairnmfnrrhaablarsttsioeittgoesrdns" \
       "alneutgmcoehoeusehelhttheycowwvtrerfadtfdroelsaibethhstuitoeatmedrtgkktdsgieltniksmrlioiihhyudkwhnehsrtylgotjeu" \
       "plhcnlpoieeirnscnthuasomeeshtpisaowotmnaeltwnseaomeonaelotewoiothopniyakeolmscsspgnodtespmmrtsoeoertnshrmaogso" \
       "sngictuncfetrympiiunnheildcmmtsoaeiaahamomaeptureptcfsbnlemiawyttetmteasossoemrktpelftpeeetnattreowdcrsmmrry" \
       "tpnneanptriufeedbrinteledmiihrnyuwtwaowihlaaihuetpwechupdmeyeebeaadoeltdtcorhansstaeyasfigayernseidonhulsveneun" \
       "chitsoeideerrlyertnorniowaanashwaelgttolrmcsopidiapgtcnhutanoeeldnmdeatfnmrgtibeaoptehtlaslnnsionhenlpitoawusy" \
       "omruaekdrmeaeiretnodmlooaiwdsooecehtaololapeetttwabynttoyeianomgnmusmrlrnsnharrgvtnriekaehfrgdanbutehsetcwikas" \
       "lprohaatotihcpernleoeeebnippucbdoelppeetitcdnnnetweisterptekbhknnscsaasnanytsogiahsneiisrlreddlrnhlewsiroori" \
       "" \
       "nhahodtsaemstnamiidileoeeaeucrtitdsesposnemolnmibetreeaacauaahnalwmnerliwwwhlgrchakinsbcenfrwtmgerhssipnmatitd" \
       "rnodnlyfojrfilhseddeellnrgoolmlhaekipoaialimekehtpehramoeiinedrdosboponroltttairnimewtestiyeptcwajoessiarvtlnl" \
       "napedehalipretstngraptnblerngotyhfhctotnrdhharhnprrhlsduondasnaeiediekuditeulsrpnfaotbsnrhtoasaopmpseoekfmtepn" \
       "aadeeeataeoieskiuhtblrtdvosestnassifartomweeotaehlmmltaerealahlmhprottpsparhlcctatmpephliehtonprhhckhetelairen" \
       "rhnilseteriauoerrlueooeaatssatllreiakudaautraundahovaeieheoiseiysypeciamiebobpnpsfpgmodtanoulhuwriulorngappst" \
       "rooteetdamossnbospghtndioerintanponrreuebaecwiattwsiahhrnmrteeeliaheciblplhbtflsaguiaaoameotutwtdtqeylmiayna" \
       "oraoeekiynenlwaoraiihyranreihtaoroeebetesucrqntrrleomsiyaeuettrtlowplenmdnenpeiefhtteggveeertrwvabboeooeies" \
       "dtpkiudadposwrhtrdnaxhopiiuhatdtebcsgyrmnaaswmehemspmhoaeselkfknnrwtoiteniuslroinpohaedlconrsntalotmoyeodt"

message = ""

iterate = int(math.sqrt(len(big_cipher)))
i = 0
while i < iterate:
    message += big_cipher[i::iterate]  # start::step and that's how we get the letters
    i+=1
print(message)
