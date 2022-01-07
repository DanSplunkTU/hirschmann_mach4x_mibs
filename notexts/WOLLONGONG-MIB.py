#
# PySNMP MIB module WOLLONGONG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wollongong/WOLLONGONG-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:41:35 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, TimeTicks, Counter32, Bits, Gauge32, Counter64, Unsigned32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "Counter32", "Bits", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises")
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
mibBuilder.exportSymbols("WOLLONGONG-MIB", twgLBOutFrames1=twgLBOutFrames1, model=model, twgLBUpTime=twgLBUpTime, os2=os2, mac=mac, sun3=sun3, twgLBCollisions=twgLBCollisions, ncr=ncr, twgLBBadFrames1=twgLBBadFrames1, twgLBOutOwnFrames1=twgLBOutOwnFrames1, twgLBInFrames2=twgLBInFrames2, lANbridgeTab=lANbridgeTab, vms5=vms5, proxy=proxy, twgLBInOwnFrames1=twgLBInOwnFrames1, twgLBInOwnFrames2=twgLBInOwnFrames2, twgLBInFrames1=twgLBInFrames1, twgLBAddr1=twgLBAddr1, twgLBOutOwnFrames2=twgLBOutOwnFrames2, twgLBReboot=twgLBReboot, twgLBOutFrames2=twgLBOutFrames2, dosruntime=dosruntime, sysV386=sysV386, att3B2=att3B2, twgLBState1=twgLBState1, wollongong=wollongong, vms4=vms4, lANbridgeEnt=lANbridgeEnt, twgLBNeigh2=twgLBNeigh2, twgLBNeigh1=twgLBNeigh1, dosroute=dosroute, twgLBStatus=twgLBStatus, twgLBState2=twgLBState2, twgLBBadFrames2=twgLBBadFrames2, dostcp=dostcp, dos=dos)
