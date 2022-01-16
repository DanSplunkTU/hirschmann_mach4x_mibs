#
# PySNMP MIB module STORMSHIELD-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ALARM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:32 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, NotificationType, Counter32, MibIdentifier, Bits, Counter64, Unsigned32, Gauge32, TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "NotificationType", "Counter32", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "Gauge32", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snsNotifications, stormshieldMIB = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "snsNotifications", "stormshieldMIB")
snsAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 5))
snsAlarm.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsAlarm.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsAlarm.setOrganization('Stormshield')
snsATable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0), )
if mibBuilder.loadTexts: snsATable.setStatus('current')
snsAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAIndex"))
if mibBuilder.loadTexts: snsAEntry.setStatus('current')
snsAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAIndex.setStatus('current')
snsATime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsATime.setStatus('current')
snsASif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASif.setStatus('current')
snsADif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADif.setStatus('current')
snsAProto = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAProto.setStatus('current')
snsASaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASaddr.setStatus('current')
snsADaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADaddr.setStatus('current')
snsASport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASport.setStatus('current')
snsADport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADport.setStatus('current')
snsASname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASname.setStatus('current')
snsADname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADname.setStatus('current')
snsAMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAMessage.setStatus('current')
snsAicmpTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1), )
if mibBuilder.loadTexts: snsAicmpTable.setStatus('current')
snsAicmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAicmpIndex"))
if mibBuilder.loadTexts: snsAicmpEntry.setStatus('current')
snsAicmpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAicmpIndex.setStatus('current')
snsAicmpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpTime.setStatus('current')
snsAicmpSif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSif.setStatus('current')
snsAicmpDif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDif.setStatus('current')
snsAicmpSaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSaddr.setStatus('current')
snsAicmpDaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDaddr.setStatus('current')
snsAicmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpType.setStatus('current')
snsAicmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpCode.setStatus('current')
snsAicmpSname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSname.setStatus('current')
snsAicmpDname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDname.setStatus('current')
snsAicmpMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpMessage.setStatus('current')
snsNotification = NotificationType((1, 3, 6, 1, 4, 1, 11256, 1, 6, 1)).setObjects(("STORMSHIELD-ALARM-MIB", "snsATime"), ("STORMSHIELD-ALARM-MIB", "snsASif"), ("STORMSHIELD-ALARM-MIB", "snsASaddr"), ("STORMSHIELD-ALARM-MIB", "snsADaddr"), ("STORMSHIELD-ALARM-MIB", "snsAMessage"))
if mibBuilder.loadTexts: snsNotification.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-ALARM-MIB", snsASname=snsASname, snsADname=snsADname, snsAicmpSaddr=snsAicmpSaddr, snsASif=snsASif, snsADport=snsADport, snsAicmpSif=snsAicmpSif, snsAicmpDif=snsAicmpDif, snsAicmpCode=snsAicmpCode, snsADaddr=snsADaddr, snsASport=snsASport, snsAlarm=snsAlarm, snsAicmpDname=snsAicmpDname, snsADif=snsADif, snsAMessage=snsAMessage, snsAicmpIndex=snsAicmpIndex, snsAicmpSname=snsAicmpSname, PYSNMP_MODULE_ID=snsAlarm, snsAicmpType=snsAicmpType, snsAicmpMessage=snsAicmpMessage, snsAicmpTime=snsAicmpTime, snsAicmpDaddr=snsAicmpDaddr, snsAicmpEntry=snsAicmpEntry, snsAEntry=snsAEntry, snsAProto=snsAProto, snsAIndex=snsAIndex, snsAicmpTable=snsAicmpTable, snsATime=snsATime, snsNotification=snsNotification, snsASaddr=snsASaddr, snsATable=snsATable)
