#
# PySNMP MIB module WOLLONGONG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wollongong/WOLLONGONG-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:21:59 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, enterprises, Bits, Gauge32, Unsigned32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, ObjectIdentity, Counter32, iso, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Bits", "Gauge32", "Unsigned32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter32", "iso", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wollongong = MibIdentifier((1, 3, 6, 1, 4, 1, 6))
model = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1))
vms4 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 1))
vms5 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 2))
sun3 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 3))
sysV386 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 4))
att3B2 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 5))
ncr = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 6))
dos = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 7))
dostcp = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 7, 1))
dosroute = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 7, 2))
dosruntime = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 7, 3))
os2 = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 8))
mac = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 1, 9))
proxy = MibIdentifier((1, 3, 6, 1, 4, 1, 6, 2))
lANbridgeTab = MibTable((1, 3, 6, 1, 4, 1, 6, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lANbridgeTab.setStatus('optional')
lANbridgeEnt = MibTableRow((1, 3, 6, 1, 4, 1, 6, 2, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lANbridgeEnt.setStatus('optional')
twgLBUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBUpTime.setStatus('optional')
twgLBNeigh1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBNeigh1.setStatus('optional')
twgLBNeigh2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBNeigh2.setStatus('optional')
twgLBInFrames1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBInFrames1.setStatus('optional')
twgLBInFrames2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBInFrames2.setStatus('optional')
twgLBOutFrames1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBOutFrames1.setStatus('optional')
twgLBOutFrames2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBOutFrames2.setStatus('optional')
twgLBBadFrames1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBBadFrames1.setStatus('optional')
twgLBBadFrames2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBBadFrames2.setStatus('optional')
twgLBCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBCollisions.setStatus('optional')
twgLBInOwnFrames1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBInOwnFrames1.setStatus('optional')
twgLBInOwnFrames2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBInOwnFrames2.setStatus('optional')
twgLBOutOwnFrames1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBOutOwnFrames1.setStatus('optional')
twgLBOutOwnFrames2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBOutOwnFrames2.setStatus('optional')
twgLBReboot = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: twgLBReboot.setStatus('optional')
twgLBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBStatus.setStatus('optional')
twgLBState1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBState1.setStatus('optional')
twgLBState2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBState2.setStatus('optional')
twgLBAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6, 2, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: twgLBAddr1.setStatus('optional')
mibBuilder.exportSymbols("WOLLONGONG-MIB", vms5=vms5, twgLBUpTime=twgLBUpTime, os2=os2, twgLBInOwnFrames2=twgLBInOwnFrames2, twgLBInFrames2=twgLBInFrames2, sysV386=sysV386, proxy=proxy, twgLBReboot=twgLBReboot, twgLBOutOwnFrames1=twgLBOutOwnFrames1, twgLBStatus=twgLBStatus, twgLBCollisions=twgLBCollisions, twgLBState1=twgLBState1, mac=mac, twgLBBadFrames1=twgLBBadFrames1, vms4=vms4, twgLBInFrames1=twgLBInFrames1, twgLBOutFrames2=twgLBOutFrames2, att3B2=att3B2, twgLBState2=twgLBState2, model=model, twgLBInOwnFrames1=twgLBInOwnFrames1, dosruntime=dosruntime, ncr=ncr, dos=dos, sun3=sun3, twgLBBadFrames2=twgLBBadFrames2, twgLBOutOwnFrames2=twgLBOutOwnFrames2, twgLBNeigh1=twgLBNeigh1, dosroute=dosroute, twgLBAddr1=twgLBAddr1, lANbridgeEnt=lANbridgeEnt, twgLBNeigh2=twgLBNeigh2, wollongong=wollongong, lANbridgeTab=lANbridgeTab, twgLBOutFrames1=twgLBOutFrames1, dostcp=dostcp)
