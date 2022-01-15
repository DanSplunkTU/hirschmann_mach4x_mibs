#
# PySNMP MIB module RMCU (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/westmountainradio/RMCU
# Produced by pysmi-1.1.8 at Sat Jan 15 18:21:53 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter32, Counter64, ObjectIdentity, IpAddress, enterprises, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ModuleIdentity, iso, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "IpAddress", "enterprises", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ModuleIdentity", "iso", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rr4005i = ModuleIdentity((1, 3, 6, 1, 4, 1, 15117, 1))
rr4005i.setRevisions(('2017-10-11 13:00',))
if mibBuilder.loadTexts: rr4005i.setLastUpdated('201710111300Z')
if mibBuilder.loadTexts: rr4005i.setOrganization('West Mountain Radio')
wmr = MibIdentifier((1, 3, 6, 1, 4, 1, 15117))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 15117, 1, 1))
control = MibIdentifier((1, 3, 6, 1, 4, 1, 15117, 1, 2))
control_ints = MibIdentifier((1, 3, 6, 1, 4, 1, 15117, 1, 4)).setLabel("control-ints")
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 15117, 1, 3))
class FixedDiv1000(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: name.setStatus('current')
version = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
build_date = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 1, 3), DisplayString()).setLabel("build-date").setMaxAccess("readonly")
if mibBuilder.loadTexts: build_date.setStatus('current')
analog1name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog1name.setStatus('current')
analog1val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog1val.setStatus('current')
analog2name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog2name.setStatus('current')
analog2val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog2val.setStatus('current')
analog3name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog3name.setStatus('current')
analog3val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog3val.setStatus('current')
analog4name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog4name.setStatus('current')
analog4val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog4val.setStatus('current')
analog5name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog5name.setStatus('current')
analog5val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog5val.setStatus('current')
analog6name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog6name.setStatus('current')
analog6val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: analog6val.setStatus('current')
digout1name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 65), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digout1name.setStatus('current')
digout1val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 66), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: digout1val.setStatus('current')
digout2name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 67), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digout2name.setStatus('current')
digout2val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 68), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: digout2val.setStatus('current')
digout3name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 69), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digout3name.setStatus('current')
digout3val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 70), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: digout3val.setStatus('current')
digout4name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 71), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digout4name.setStatus('current')
digout4val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 72), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: digout4val.setStatus('current')
digout5name = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 73), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: digout5name.setStatus('current')
digout5val = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 2, 74), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: digout5val.setStatus('current')
analog1val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 1), FixedDiv1000()).setLabel("analog1val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog1val_int.setStatus('current')
analog2val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 2), FixedDiv1000()).setLabel("analog2val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog2val_int.setStatus('current')
analog3val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 3), FixedDiv1000()).setLabel("analog3val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog3val_int.setStatus('current')
analog4val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 4), FixedDiv1000()).setLabel("analog4val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog4val_int.setStatus('current')
analog5val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 5), FixedDiv1000()).setLabel("analog5val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog5val_int.setStatus('current')
analog6val_int = MibScalar((1, 3, 6, 1, 4, 1, 15117, 1, 4, 6), FixedDiv1000()).setLabel("analog6val-int").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog6val_int.setStatus('current')
trap_auth = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 1)).setLabel("trap-auth")
if mibBuilder.loadTexts: trap_auth.setStatus('current')
trap_analog_over1 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 2)).setLabel("trap-analog-over1").setObjects(("RMCU", "name"), ("RMCU", "analog1val"))
if mibBuilder.loadTexts: trap_analog_over1.setStatus('current')
trap_analog_over2 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 3)).setLabel("trap-analog-over2").setObjects(("RMCU", "name"), ("RMCU", "analog2val"))
if mibBuilder.loadTexts: trap_analog_over2.setStatus('current')
trap_analog_over3 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 4)).setLabel("trap-analog-over3").setObjects(("RMCU", "name"), ("RMCU", "analog3val"))
if mibBuilder.loadTexts: trap_analog_over3.setStatus('current')
trap_analog_over4 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 5)).setLabel("trap-analog-over4").setObjects(("RMCU", "name"), ("RMCU", "analog4val"))
if mibBuilder.loadTexts: trap_analog_over4.setStatus('current')
trap_analog_over5 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 6)).setLabel("trap-analog-over5").setObjects(("RMCU", "name"), ("RMCU", "analog5val"))
if mibBuilder.loadTexts: trap_analog_over5.setStatus('current')
trap_analog_over6 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 7)).setLabel("trap-analog-over6").setObjects(("RMCU", "name"), ("RMCU", "analog6val"))
if mibBuilder.loadTexts: trap_analog_over6.setStatus('current')
trap_analog_under6 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 23)).setLabel("trap-analog-under6").setObjects(("RMCU", "name"), ("RMCU", "analog6val"))
if mibBuilder.loadTexts: trap_analog_under6.setStatus('current')
trap_poweron = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 34)).setLabel("trap-poweron").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_poweron.setStatus('current')
trap_test = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 52)).setLabel("trap-test").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_test.setStatus('current')
trap_digout_inactive1 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 72)).setLabel("trap-digout-inactive1").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_inactive1.setStatus('current')
trap_digout_inactive2 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 73)).setLabel("trap-digout-inactive2").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_inactive2.setStatus('current')
trap_digout_inactive3 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 74)).setLabel("trap-digout-inactive3").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_inactive3.setStatus('current')
trap_digout_inactive4 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 75)).setLabel("trap-digout-inactive4").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_inactive4.setStatus('current')
trap_digout_inactive5 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 76)).setLabel("trap-digout-inactive5").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_inactive5.setStatus('current')
trap_digout_active1 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 88)).setLabel("trap-digout-active1").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_active1.setStatus('current')
trap_digout_active2 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 89)).setLabel("trap-digout-active2").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_active2.setStatus('current')
trap_digout_active3 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 90)).setLabel("trap-digout-active3").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_active3.setStatus('current')
trap_digout_active4 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 91)).setLabel("trap-digout-active4").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_active4.setStatus('current')
trap_digout_active5 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 92)).setLabel("trap-digout-active5").setObjects(("RMCU", "name"))
if mibBuilder.loadTexts: trap_digout_active5.setStatus('current')
trap_analog_urecover6 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 109)).setLabel("trap-analog-urecover6").setObjects(("RMCU", "name"), ("RMCU", "analog6val"))
if mibBuilder.loadTexts: trap_analog_urecover6.setStatus('current')
trap_analog_orecover1 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 120)).setLabel("trap-analog-orecover1").setObjects(("RMCU", "name"), ("RMCU", "analog1val"))
if mibBuilder.loadTexts: trap_analog_orecover1.setStatus('current')
trap_analog_orecover2 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 121)).setLabel("trap-analog-orecover2").setObjects(("RMCU", "name"), ("RMCU", "analog2val"))
if mibBuilder.loadTexts: trap_analog_orecover2.setStatus('current')
trap_analog_orecover3 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 122)).setLabel("trap-analog-orecover3").setObjects(("RMCU", "name"), ("RMCU", "analog3val"))
if mibBuilder.loadTexts: trap_analog_orecover3.setStatus('current')
trap_analog_orecover4 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 123)).setLabel("trap-analog-orecover4").setObjects(("RMCU", "name"), ("RMCU", "analog4val"))
if mibBuilder.loadTexts: trap_analog_orecover4.setStatus('current')
trap_analog_orecover5 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 124)).setLabel("trap-analog-orecover5").setObjects(("RMCU", "name"), ("RMCU", "analog5val"))
if mibBuilder.loadTexts: trap_analog_orecover5.setStatus('current')
trap_analog_orecover6 = NotificationType((1, 3, 6, 1, 4, 1, 15117, 1, 3, 125)).setLabel("trap-analog-orecover6").setObjects(("RMCU", "name"), ("RMCU", "analog6val"))
if mibBuilder.loadTexts: trap_analog_orecover6.setStatus('current')
mibBuilder.exportSymbols("RMCU", trap_digout_inactive3=trap_digout_inactive3, control=control, digout5val=digout5val, rr4005i=rr4005i, analog6val_int=analog6val_int, trap_analog_orecover4=trap_analog_orecover4, name=name, digout3val=digout3val, trap_analog_over1=trap_analog_over1, product=product, analog2val=analog2val, analog3val=analog3val, analog4name=analog4name, analog5val=analog5val, digout3name=digout3name, analog1name=analog1name, analog5name=analog5name, version=version, wmr=wmr, trap_digout_inactive2=trap_digout_inactive2, trap_digout_active1=trap_digout_active1, PYSNMP_MODULE_ID=rr4005i, digout2name=digout2name, trap_analog_over4=trap_analog_over4, analog5val_int=analog5val_int, trap_analog_over2=trap_analog_over2, trap_auth=trap_auth, analog3name=analog3name, digout4val=digout4val, trap_test=trap_test, digout1name=digout1name, analog6val=analog6val, analog4val_int=analog4val_int, trap_digout_inactive4=trap_digout_inactive4, trap_digout_inactive5=trap_digout_inactive5, build_date=build_date, trap_analog_over5=trap_analog_over5, trap_analog_over3=trap_analog_over3, digout4name=digout4name, trap_digout_active4=trap_digout_active4, digout2val=digout2val, trap_analog_orecover6=trap_analog_orecover6, traps=traps, analog4val=analog4val, analog2val_int=analog2val_int, control_ints=control_ints, digout1val=digout1val, analog1val_int=analog1val_int, analog3val_int=analog3val_int, analog1val=analog1val, trap_digout_active3=trap_digout_active3, trap_analog_under6=trap_analog_under6, FixedDiv1000=FixedDiv1000, trap_poweron=trap_poweron, trap_analog_orecover3=trap_analog_orecover3, analog2name=analog2name, trap_analog_urecover6=trap_analog_urecover6, trap_analog_orecover2=trap_analog_orecover2, trap_digout_active5=trap_digout_active5, analog6name=analog6name, trap_digout_active2=trap_digout_active2, trap_analog_over6=trap_analog_over6, trap_analog_orecover1=trap_analog_orecover1, digout5name=digout5name, trap_digout_inactive1=trap_digout_inactive1, trap_analog_orecover5=trap_analog_orecover5)
