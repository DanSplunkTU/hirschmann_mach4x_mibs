#
# PySNMP MIB module STORMSHIELD-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-ALARM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:48 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, iso, IpAddress, ModuleIdentity, Bits, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "ModuleIdentity", "Bits", "Unsigned32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stormshieldMIB, snsNotifications = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB", "snsNotifications")
snsAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 5))
snsAlarm.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsAlarm.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsAlarm.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsAlarm.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsAlarm.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsAlarm.setDescription('stormshield alarm MIBs')
snsATable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0), )
if mibBuilder.loadTexts: snsATable.setStatus('current')
if mibBuilder.loadTexts: snsATable.setDescription('Alarm Table')
snsAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAIndex"))
if mibBuilder.loadTexts: snsAEntry.setStatus('current')
if mibBuilder.loadTexts: snsAEntry.setDescription('Alarm table entry')
snsAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAIndex.setStatus('current')
if mibBuilder.loadTexts: snsAIndex.setDescription('Index of each line in table')
snsATime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsATime.setStatus('current')
if mibBuilder.loadTexts: snsATime.setDescription('alarm date')
snsASif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASif.setStatus('current')
if mibBuilder.loadTexts: snsASif.setDescription('source interface')
snsADif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADif.setStatus('current')
if mibBuilder.loadTexts: snsADif.setDescription('destination interface')
snsAProto = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAProto.setStatus('current')
if mibBuilder.loadTexts: snsAProto.setDescription('IP protocol')
snsASaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASaddr.setStatus('current')
if mibBuilder.loadTexts: snsASaddr.setDescription('source IP address')
snsADaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADaddr.setStatus('current')
if mibBuilder.loadTexts: snsADaddr.setDescription('destination IP address')
snsASport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASport.setStatus('current')
if mibBuilder.loadTexts: snsASport.setDescription('Source port')
snsADport = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADport.setStatus('current')
if mibBuilder.loadTexts: snsADport.setDescription('Destination port')
snsASname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsASname.setStatus('current')
if mibBuilder.loadTexts: snsASname.setDescription('IP source name')
snsADname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsADname.setStatus('current')
if mibBuilder.loadTexts: snsADname.setDescription('IP destination name')
snsAMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 0, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAMessage.setStatus('current')
if mibBuilder.loadTexts: snsAMessage.setDescription('Alarm Message')
snsAicmpTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1), )
if mibBuilder.loadTexts: snsAicmpTable.setStatus('current')
if mibBuilder.loadTexts: snsAicmpTable.setDescription('ICMP alarm table')
snsAicmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1), ).setIndexNames((0, "STORMSHIELD-ALARM-MIB", "snsAicmpIndex"))
if mibBuilder.loadTexts: snsAicmpEntry.setStatus('current')
if mibBuilder.loadTexts: snsAicmpEntry.setDescription('Entry in the snsAicmpTable.')
snsAicmpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 0), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: snsAicmpIndex.setStatus('current')
if mibBuilder.loadTexts: snsAicmpIndex.setDescription('A unique value for phase one table.  Its value\n         ranges between 1 and 65535 and may not be contigous.\n         the index has no other meaning but a pure index')
snsAicmpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpTime.setStatus('current')
if mibBuilder.loadTexts: snsAicmpTime.setDescription('Alarm date')
snsAicmpSif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSif.setStatus('current')
if mibBuilder.loadTexts: snsAicmpSif.setDescription('source interface')
snsAicmpDif = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDif.setStatus('current')
if mibBuilder.loadTexts: snsAicmpDif.setDescription('destination interface')
snsAicmpSaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSaddr.setStatus('current')
if mibBuilder.loadTexts: snsAicmpSaddr.setDescription('IP source address')
snsAicmpDaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDaddr.setStatus('current')
if mibBuilder.loadTexts: snsAicmpDaddr.setDescription('IP destination address')
snsAicmpType = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpType.setStatus('current')
if mibBuilder.loadTexts: snsAicmpType.setDescription('ICMP type')
snsAicmpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpCode.setStatus('current')
if mibBuilder.loadTexts: snsAicmpCode.setDescription('ICMP code')
snsAicmpSname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpSname.setStatus('current')
if mibBuilder.loadTexts: snsAicmpSname.setDescription('IP source name')
snsAicmpDname = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpDname.setStatus('current')
if mibBuilder.loadTexts: snsAicmpDname.setDescription('IP destination name')
snsAicmpMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 5, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAicmpMessage.setStatus('current')
if mibBuilder.loadTexts: snsAicmpMessage.setDescription('Alarm message')
snsNotification = NotificationType((1, 3, 6, 1, 4, 1, 11256, 1, 6, 1)).setObjects(("STORMSHIELD-ALARM-MIB", "snsATime"), ("STORMSHIELD-ALARM-MIB", "snsASif"), ("STORMSHIELD-ALARM-MIB", "snsASaddr"), ("STORMSHIELD-ALARM-MIB", "snsADaddr"), ("STORMSHIELD-ALARM-MIB", "snsAMessage"))
if mibBuilder.loadTexts: snsNotification.setStatus('current')
if mibBuilder.loadTexts: snsNotification.setDescription('notification')
mibBuilder.exportSymbols("STORMSHIELD-ALARM-MIB", snsASport=snsASport, snsAicmpType=snsAicmpType, snsADif=snsADif, snsAicmpTime=snsAicmpTime, snsAicmpDname=snsAicmpDname, snsAicmpDaddr=snsAicmpDaddr, snsNotification=snsNotification, snsATable=snsATable, snsAicmpIndex=snsAicmpIndex, snsAicmpEntry=snsAicmpEntry, snsASif=snsASif, snsAicmpSif=snsAicmpSif, snsASaddr=snsASaddr, snsAicmpCode=snsAicmpCode, snsAEntry=snsAEntry, snsAicmpTable=snsAicmpTable, snsADname=snsADname, snsAicmpDif=snsAicmpDif, snsAIndex=snsAIndex, snsAProto=snsAProto, snsAicmpSaddr=snsAicmpSaddr, snsAMessage=snsAMessage, snsAicmpMessage=snsAicmpMessage, snsADaddr=snsADaddr, snsATime=snsATime, snsAicmpSname=snsAicmpSname, PYSNMP_MODULE_ID=snsAlarm, snsASname=snsASname, snsAlarm=snsAlarm, snsADport=snsADport)
