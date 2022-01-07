#
# PySNMP MIB module ATM-SOFT-PVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ATM-SOFT-PVC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmVclVpi, atmVplVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVplVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32", "enterprises")
RowStatus, TimeStamp, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TruthValue", "DisplayString", "TextualConvention")
atmSoftPvcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 353, 5, 5, 1))
atmSoftPvcMIB.setRevisions(('1997-03-01 00:00', '1996-06-21 00:00',))
if mibBuilder.loadTexts: atmSoftPvcMIB.setLastUpdated('9703010000Z')
if mibBuilder.loadTexts: atmSoftPvcMIB.setOrganization('The ATM Forum.')
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumNetworkManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5))
atmfSoftPvc = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5))
atmSoftPvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1))
atmSoftPvcMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
atmSoftPvcBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1))
atmSoftPvcCallFailuresTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSoftPvcCallFailuresTrapEnable.setStatus('current')
atmSoftPvcCallFailures = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCallFailures.setStatus('current')
atmSoftPvcCurrentlyFailingSoftPVccs = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCurrentlyFailingSoftPVccs.setStatus('current')
atmSoftPvcCurrentlyFailingSoftPVpcs = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPvcCurrentlyFailingSoftPVpcs.setStatus('current')
atmSoftPvcNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSoftPvcNotificationInterval.setStatus('current')
atmSoftPVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2), )
if mibBuilder.loadTexts: atmSoftPVccTable.setStatus('current')
atmSoftPVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"))
if mibBuilder.loadTexts: atmSoftPVccEntry.setStatus('current')
atmSoftPVccLeafReference = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: atmSoftPVccLeafReference.setStatus('current')
atmSoftPVccTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetAddress.setStatus('current')
atmSoftPVccTargetSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("any", 2))).clone('required')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetSelectType.setStatus('current')
atmSoftPVccTargetVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetVpi.setStatus('current')
atmSoftPVccTargetVci = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccTargetVci.setStatus('current')
atmSoftPVccLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccLastReleaseCause.setStatus('current')
atmSoftPVccLastReleaseDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccLastReleaseDiagnostic.setStatus('current')
atmSoftPVccOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("establishmentInProgress", 2), ("connected", 3), ("retriesExhausted", 4), ("noAddressSupplied", 5), ("lowerLayerDown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccOperStatus.setStatus('current')
atmSoftPVccRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRestart.setStatus('current')
atmSoftPVccRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryInterval.setStatus('current')
atmSoftPVccRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccRetryTimer.setStatus('current')
atmSoftPVccRetryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryThreshold.setStatus('current')
atmSoftPVccRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVccRetryFailures.setStatus('current')
atmSoftPVccRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRetryLimit.setStatus('current')
atmSoftPVccRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 2, 1, 15), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVccRowStatus.setStatus('current')
atmSoftPVpcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3), )
if mibBuilder.loadTexts: atmSoftPVpcTable.setStatus('current')
atmSoftPVpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVplVpi"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"))
if mibBuilder.loadTexts: atmSoftPVpcEntry.setStatus('current')
atmSoftPVpcLeafReference = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63535)))
if mibBuilder.loadTexts: atmSoftPVpcLeafReference.setStatus('current')
atmSoftPVpcTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetAddress.setStatus('current')
atmSoftPVpcTargetSelectType = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("any", 2))).clone('required')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetSelectType.setStatus('current')
atmSoftPVpcTargetVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcTargetVpi.setStatus('current')
atmSoftPVpcLastReleaseCause = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcLastReleaseCause.setStatus('current')
atmSoftPVpcLastReleaseDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcLastReleaseDiagnostic.setStatus('current')
atmSoftPVpcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("establishmentInProgress", 2), ("connected", 3), ("retriesExhausted", 4), ("noAddressSupplied", 5), ("lowerLayerDown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcOperStatus.setStatus('current')
atmSoftPVpcRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restart", 1), ("noop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRestart.setStatus('current')
atmSoftPVpcRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(10)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryInterval.setStatus('current')
atmSoftPVpcRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcRetryTimer.setStatus('current')
atmSoftPVpcRetryThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryThreshold.setStatus('current')
atmSoftPVpcRetryFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSoftPVpcRetryFailures.setStatus('current')
atmSoftPVpcRetryLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRetryLimit.setStatus('current')
atmSoftPVpcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 3, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmSoftPVpcRowStatus.setStatus('current')
atmInterfaceSoftPvcAddressTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4), )
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressTable.setStatus('current')
atmInterfaceSoftPvcAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddress"))
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressEntry.setStatus('current')
atmInterfaceSoftPvcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 1), AtmAddr())
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddress.setStatus('current')
atmInterfaceSoftPvcAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmInterfaceSoftPvcAddressRowStatus.setStatus('current')
atmCurrentlyFailingSoftPVccTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5), )
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccTable.setStatus('current')
atmCurrentlyFailingSoftPVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVccLeafReference"))
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccEntry.setStatus('current')
atmCurrentlyFailingSoftPVccTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 5, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVccTimeStamp.setStatus('current')
atmCurrentlyFailingSoftPVpcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6), )
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcTable.setStatus('current')
atmCurrentlyFailingSoftPVpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-SOFT-PVC-MIB", "atmSoftPVpcLeafReference"))
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcEntry.setStatus('current')
atmCurrentlyFailingSoftPVpcTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 1, 6, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingSoftPVpcTimeStamp.setStatus('current')
atmSoftPvcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1))
atmSoftPvcTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0))
atmSoftPvcCallFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
if mibBuilder.loadTexts: atmSoftPvcCallFailuresTrap.setStatus('current')
atmSoftPvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3))
atmSoftPvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1))
atmSoftPvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2))
atmSoftPvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 1, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcBaseMIBGroup"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcVccMIBGroup"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcAddressMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcMIBCompliance = atmSoftPvcMIBCompliance.setStatus('current')
atmSoftPvcBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailuresTrapEnable"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcNotificationInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcBaseMIBGroup = atmSoftPvcBaseMIBGroup.setStatus('current')
atmSoftPvcVccMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 2)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetAddress"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetSelectType"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVpi"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccTargetVci"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseCause"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccLastReleaseDiagnostic"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccOperStatus"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRestart"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryInterval"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryTimer"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryThreshold"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRetryLimit"), ("ATM-SOFT-PVC-MIB", "atmSoftPVccRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcVccMIBGroup = atmSoftPvcVccMIBGroup.setStatus('current')
atmSoftPvcVpcMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 3)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetAddress"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetSelectType"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcTargetVpi"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseCause"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcLastReleaseDiagnostic"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcOperStatus"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRestart"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryInterval"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryTimer"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryThreshold"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRetryLimit"), ("ATM-SOFT-PVC-MIB", "atmSoftPVpcRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcVpcMIBGroup = atmSoftPvcVpcMIBGroup.setStatus('current')
atmSoftPvcAddressMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 4)).setObjects(("ATM-SOFT-PVC-MIB", "atmInterfaceSoftPvcAddressRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSoftPvcAddressMIBGroup = atmSoftPvcAddressMIBGroup.setStatus('current')
atmCurrentlyFailingSoftPVccMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 5)).setObjects(("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVccTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmCurrentlyFailingSoftPVccMIBGroup = atmCurrentlyFailingSoftPVccMIBGroup.setStatus('current')
atmCurrentlyFailingSoftPVpcMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 3, 2, 6)).setObjects(("ATM-SOFT-PVC-MIB", "atmCurrentlyFailingSoftPVpcTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmCurrentlyFailingSoftPVpcMIBGroup = atmCurrentlyFailingSoftPVpcMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ATM-SOFT-PVC-MIB", PYSNMP_MODULE_ID=atmSoftPvcMIB, atmSoftPVpcTargetSelectType=atmSoftPVpcTargetSelectType, atmSoftPvcMIB=atmSoftPvcMIB, atmSoftPVpcTargetAddress=atmSoftPVpcTargetAddress, atmSoftPvcCallFailuresTrapEnable=atmSoftPvcCallFailuresTrapEnable, atmInterfaceSoftPvcAddressTable=atmInterfaceSoftPvcAddressTable, atmInterfaceSoftPvcAddress=atmInterfaceSoftPvcAddress, atmCurrentlyFailingSoftPVpcTimeStamp=atmCurrentlyFailingSoftPVpcTimeStamp, atmSoftPVccLeafReference=atmSoftPVccLeafReference, atmCurrentlyFailingSoftPVpcTable=atmCurrentlyFailingSoftPVpcTable, atmSoftPVccRetryFailures=atmSoftPVccRetryFailures, atmSoftPVpcLastReleaseDiagnostic=atmSoftPVpcLastReleaseDiagnostic, atmSoftPVccLastReleaseDiagnostic=atmSoftPVccLastReleaseDiagnostic, atmCurrentlyFailingSoftPVpcMIBGroup=atmCurrentlyFailingSoftPVpcMIBGroup, atmSoftPVccRowStatus=atmSoftPVccRowStatus, atmSoftPvcMIBGroups=atmSoftPvcMIBGroups, atmSoftPvcBaseMIBGroup=atmSoftPvcBaseMIBGroup, atmSoftPVpcLeafReference=atmSoftPVpcLeafReference, atmSoftPVccTargetVpi=atmSoftPVccTargetVpi, atmCurrentlyFailingSoftPVpcEntry=atmCurrentlyFailingSoftPVpcEntry, atmSoftPvcVpcMIBGroup=atmSoftPvcVpcMIBGroup, atmSoftPVccEntry=atmSoftPVccEntry, atmSoftPVpcRestart=atmSoftPVpcRestart, atmSoftPVpcRetryInterval=atmSoftPVpcRetryInterval, atmSoftPvcCurrentlyFailingSoftPVccs=atmSoftPvcCurrentlyFailingSoftPVccs, atmSoftPVpcTargetVpi=atmSoftPVpcTargetVpi, atmSoftPVpcRetryLimit=atmSoftPVpcRetryLimit, atmSoftPvcCallFailuresTrap=atmSoftPvcCallFailuresTrap, atmCurrentlyFailingSoftPVccMIBGroup=atmCurrentlyFailingSoftPVccMIBGroup, atmInterfaceSoftPvcAddressEntry=atmInterfaceSoftPvcAddressEntry, atmSoftPVccTargetSelectType=atmSoftPVccTargetSelectType, atmCurrentlyFailingSoftPVccEntry=atmCurrentlyFailingSoftPVccEntry, atmSoftPvcMIBObjects=atmSoftPvcMIBObjects, atmSoftPVccRetryThreshold=atmSoftPVccRetryThreshold, atmInterfaceSoftPvcAddressRowStatus=atmInterfaceSoftPvcAddressRowStatus, atmCurrentlyFailingSoftPVccTimeStamp=atmCurrentlyFailingSoftPVccTimeStamp, atmSoftPVccRetryLimit=atmSoftPVccRetryLimit, atmSoftPVpcLastReleaseCause=atmSoftPVpcLastReleaseCause, AtmAddr=AtmAddr, atmSoftPVpcOperStatus=atmSoftPVpcOperStatus, atmSoftPVccTable=atmSoftPVccTable, atmSoftPvcCallFailures=atmSoftPvcCallFailures, atmSoftPvcTraps=atmSoftPvcTraps, atmfSoftPvc=atmfSoftPvc, atmSoftPvcBaseGroup=atmSoftPvcBaseGroup, atmSoftPvcCurrentlyFailingSoftPVpcs=atmSoftPvcCurrentlyFailingSoftPVpcs, atmSoftPVccRestart=atmSoftPVccRestart, atmSoftPVpcRetryFailures=atmSoftPVpcRetryFailures, atmSoftPvcMIBTraps=atmSoftPvcMIBTraps, atmSoftPVccRetryInterval=atmSoftPVccRetryInterval, atmSoftPVccRetryTimer=atmSoftPVccRetryTimer, atmForumNetworkManagement=atmForumNetworkManagement, atmSoftPVpcTable=atmSoftPVpcTable, atmSoftPVpcEntry=atmSoftPVpcEntry, atmSoftPvcMIBCompliance=atmSoftPvcMIBCompliance, atmSoftPvcVccMIBGroup=atmSoftPvcVccMIBGroup, atmSoftPVpcRetryTimer=atmSoftPVpcRetryTimer, atmSoftPVpcRetryThreshold=atmSoftPVpcRetryThreshold, atmSoftPVccOperStatus=atmSoftPVccOperStatus, atmSoftPVccTargetVci=atmSoftPVccTargetVci, atmSoftPvcMIBCompliances=atmSoftPvcMIBCompliances, atmForum=atmForum, atmSoftPvcNotificationInterval=atmSoftPvcNotificationInterval, atmCurrentlyFailingSoftPVccTable=atmCurrentlyFailingSoftPVccTable, atmSoftPvcMIBConformance=atmSoftPvcMIBConformance, atmSoftPvcTrapsPrefix=atmSoftPvcTrapsPrefix, atmSoftPVccTargetAddress=atmSoftPVccTargetAddress, atmSoftPvcAddressMIBGroup=atmSoftPvcAddressMIBGroup, atmSoftPVpcRowStatus=atmSoftPVpcRowStatus, atmSoftPVccLastReleaseCause=atmSoftPVccLastReleaseCause)
