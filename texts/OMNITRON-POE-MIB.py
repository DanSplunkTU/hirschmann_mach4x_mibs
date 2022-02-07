#
# PySNMP MIB module OMNITRON-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/omnitron/OMNITRON-POE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:20 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
omnitron, OstFloatValue, OstPortSingleIndex = mibBuilder.importSymbols("OMNITRON-TC-MIB", "omnitron", "OstFloatValue", "OstPortSingleIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Counter32, Integer32, Counter64, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Counter32", "Integer32", "Counter64", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "NotificationType", "MibIdentifier")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
omnitronPoeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7342, 15))
omnitronPoeMib.setRevisions(('2015-01-19 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: omnitronPoeMib.setRevisionsDescriptions(('Initial version of v5.2 MIB.\n                ',))
if mibBuilder.loadTexts: omnitronPoeMib.setLastUpdated('201501191200Z')
if mibBuilder.loadTexts: omnitronPoeMib.setOrganization('Omnitron Systems Technology, Inc.')
if mibBuilder.loadTexts: omnitronPoeMib.setContactInfo('Omnitron Systems Technology, Inc.\n                  38 Tesla\n                  Irvine, CA 92618-4670\n                  USA\n\n             Tel: (949) 250 6510\n             Fax: (949) 250 6514\n          E-mail: info@omnitron-systems.com\n   International: +1 949 250 6510\n\n                  Technical Support and Customer Service\n             Tel: (800) 675 8410\n          E-mail: support@omnitron-systems.com\n   International: +1 949 250 6510')
if mibBuilder.loadTexts: omnitronPoeMib.setDescription('Omnitron PoE MIB for use with iConverter Management Modules v5.2\n             and NetOutlook.\n\n             Copyright 2015 Omnitron Systems Technology, Inc.\n             All rights reserved.\n            ')
ostPoeGlobalCfgTable = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 1))
ostPoeGlobalCfgPwrLimitationEnable = MibScalar((1, 3, 6, 1, 4, 1, 7342, 15, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoeGlobalCfgPwrLimitationEnable.setStatus('current')
if mibBuilder.loadTexts: ostPoeGlobalCfgPwrLimitationEnable.setDescription("This object specifies whether the PoE PSE power limiting function is enabled.\n\n        The value 'true' indicates that PoE PSE limiting is enabled.\n\n        The value 'false' indicates that PoE PSE limiting is disabled.\n       ")
ostPoeGlobalCfgTotalPwr = MibScalar((1, 3, 6, 1, 4, 1, 7342, 15, 1, 2), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoeGlobalCfgTotalPwr.setStatus('current')
if mibBuilder.loadTexts: ostPoeGlobalCfgTotalPwr.setDescription('This object indicates the total power sourced in Watts.\n       ')
ostPoePortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 7342, 15, 2), )
if mibBuilder.loadTexts: ostPoePortCfgTable.setStatus('current')
if mibBuilder.loadTexts: ostPoePortCfgTable.setDescription('This table supports the port PoE configurations.')
ostPoePortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1), ).setIndexNames((0, "OMNITRON-POE-MIB", "ostPoePortCfgIndex"))
if mibBuilder.loadTexts: ostPoePortCfgEntry.setStatus('current')
if mibBuilder.loadTexts: ostPoePortCfgEntry.setDescription('This is a PoE port configuration table entry.')
ostPoePortCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 1), OstPortSingleIndex())
if mibBuilder.loadTexts: ostPoePortCfgIndex.setStatus('current')
if mibBuilder.loadTexts: ostPoePortCfgIndex.setDescription('An index that is used to identify a specific PoE port number.')
ostPoePortPseEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pseDisabled", 1), ("pseEnabled", 2))).clone('pseEnabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPseEnable.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPseEnable.setDescription('This object is the PoE PSE port enable.\n\n        pseDisabled(1)           PSE power source is disabled\n        pseEnabled(2)            PSE power source is enabled\n       ')
ostPoePortPse60wMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("pse60wNotAvail", 0), ("pse60wAuto", 1), ("pse60wForce", 2))).clone('pse60wAuto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPse60wMode.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPse60wMode.setDescription('The object is the PoE PSE 60W mode enable. This is the same control as\n        the physical DIP switch.\n\n        pse60wNotAvail           PSE 60W function not available\n        pse60wAuto(1)            PSE 60W auto mode enabled\n        pse60wForce(2)           PSE 60W force mode enabled\n       ')
ostPoePortPdMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("pdModeNotDetected", 1), ("pdModeNotClassified", 2), ("pdModeFailure", 3), ("pdModeClass0", 4), ("pdModeClass1", 5), ("pdModeClass2", 6), ("pdModeClass3", 7), ("pdModeClass4", 8), ("pdMode60W", 9))).clone('pdModeNotDetected')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPdMode.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPdMode.setDescription('This object is the PoE PD classification mode.\n\n        pdModeNotDetected(1)     PD is not detected\n        pdModeNotClassified(2)   PD is not classified\n        pdModeFailure(3)         PD classification failure\n        pdModeClass0(4)          PD is 802.3af Class 0 15W device\n        pdModeClass1(5)          PD is 802.3af Class 1 4W device\n        pdModeClass2(6)          PD is 802.3af Class 2 7W device\n        pdModeClass3(7)          PD is 802.3af Class 3 15W device\n        pdModeClass4(8)          PD is 802.3at Class 4 30W device\n        pdMode60W(9)             PD is 60W device\n       ')
ostPoePortPseVoltageSupplied = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 5), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPseVoltageSupplied.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPseVoltageSupplied.setDescription('This object indicates the voltage output from the PSE port in volts.\n       ')
ostPoePortPseCurrentSupplied = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 6), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPseCurrentSupplied.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPseCurrentSupplied.setDescription('This object indicates the current output from the PSE port in mA\n        (milliamps).\n       ')
ostPoePortPseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("pdNormal", 2), ("pdOverCurrent", 3), ("pdBrownOut", 4), ("pdInsufficientPower", 5))).clone('notApplicable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPseStatus.setStatus('current')
if mibBuilder.loadTexts: ostPoePortPseStatus.setDescription('This object is the PoE PSE port status.\n\n        notApplicable(1)        PD device not connected or port disabled\n        pdNormal(2)             PD device is being powered fully\n        pdOverCurrent(3)        PD device is consuming too much current\n        pdBrownOut(4)           PD device is not fully powered\n        pdInsufficientPower(5)  PD device not powered due to lack of power\n\n        A write to this object restarts the PSE function and classification.\n       ')
ostPoePortHeartbeatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("heartbeatDisabled", 1), ("heartbeatEnabled", 2))).clone('heartbeatDisabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatEnable.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatEnable.setDescription('This object is the PoE PSE heartbeat enable.\n\n        heartbeatDisabled(1)     PSE PD heartbeat is disabled\n        heartbeatEnabled(2)      PSE PD heartbeat is enabled\n       ')
ostPoePortHeartbeatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 9), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatIpAddress.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatIpAddress.setDescription('This object is the PoE PD heartbeat IP address to ping.\n       ')
ostPoePortHeartbeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatInterval.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatInterval.setDescription('This object is the PoE PSE PD heartbeat transmission interval in seconds.\n       ')
ostPoePortHeartbeatErrorDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorDetection.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorDetection.setDescription('This object is the PoE PSE PD heartbeat number of consecutively lost\n        heartbeat pings before an errored condition is declared. The number\n        of consecutive error counts is cleared when a valid heartbeat\n        response is received.\n       ')
ostPoePortHeartbeatErrorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errorLostIgnored", 1), ("errorRestart", 2), ("errorShutdown", 3))).clone('errorLostIgnored')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorAction.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorAction.setDescription('This object is the PoE PSE heartbeat errored condition action.\n\n        errorLostIgnored(1)      PD heartbeat errored condition is ignored\n        errorRestart(2)          PD heartbeat errored condition results\n                                   in a restart\n        errorShutdown(3)         PD heartbeat errored condition results\n                                   in a shutdown (power removed)\n       ')
ostPoePortHeartbeatNumberRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatNumberRestarts.setStatus('current')
if mibBuilder.loadTexts: ostPoePortHeartbeatNumberRestarts.setDescription("This object is the PoE PSE PD number of restarts when an errored\n        hearbeat condition occurs. This object is only used when\n        ostPoePortHeartbeatErrorAction is configured as 'errorRestart'\n\n        A value of zero indicates restarts never stop.\n       ")
ostPoEPortHeartbeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("heartbeatDisabled", 1), ("heartbeatAvailable", 2), ("heartbeatErrored", 3), ("heartbeatRestart", 4), ("heartbeatShutdown", 5))).clone('heartbeatDisabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoEPortHeartbeatStatus.setStatus('current')
if mibBuilder.loadTexts: ostPoEPortHeartbeatStatus.setDescription('This object is the PoE PSE PD heartbeat status.\n\n        heartbeatDisabled(1)    PSE PD heartbeat is disabled\n        heartbeatAvailable(2)   PSE PD heartbeats are being received\n        heartbeatErrored(3)     PSE PD heartbeat is in an errored condition\n        heartbeatRestart(4)     PSE PD heartbeat error has caused a PSE restart\n        heartbeatShutdown(5)    PSE PD heartbeat error has caused a PSE shutdown\n       ')
ostPoEPortHeartbeatDeferTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoEPortHeartbeatDeferTime.setStatus('current')
if mibBuilder.loadTexts: ostPoEPortHeartbeatDeferTime.setDescription('This object is the PoE heartbeat PSE PD heartbeat transmission delay\n        interval in seconds after the port has been reenabled. The delay is\n        the amount of time after power has been applied before the heartbeat\n        function starts and hence the detection of heartbeat errors.\n       ')
ostPoeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 3))
ostPoeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 4))
ostPoeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7342, 15, 4, 1)).setObjects(("OMNITRON-POE-MIB", "ostPoeGlobalCfgPwrLimitationEnable"), ("OMNITRON-POE-MIB", "ostPoeGlobalCfgTotalPwr"), ("OMNITRON-POE-MIB", "ostPoePortPseEnable"), ("OMNITRON-POE-MIB", "ostPoePortPse60wMode"), ("OMNITRON-POE-MIB", "ostPoePortPdMode"), ("OMNITRON-POE-MIB", "ostPoePortPseVoltageSupplied"), ("OMNITRON-POE-MIB", "ostPoePortPseCurrentSupplied"), ("OMNITRON-POE-MIB", "ostPoePortPseStatus"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatEnable"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatIpAddress"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatInterval"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorDetection"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorAction"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatNumberRestarts"), ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatStatus"), ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatDeferTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ostPoeGroup = ostPoeGroup.setStatus('current')
if mibBuilder.loadTexts: ostPoeGroup.setDescription('Mandatory objects for the PoE functional group.')
ostPoeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7342, 15, 3, 2)).setObjects(("OMNITRON-POE-MIB", "ostPoeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ostPoeCompliance = ostPoeCompliance.setStatus('current')
if mibBuilder.loadTexts: ostPoeCompliance.setDescription('The compliance statement for the Omnitron PoE MIB.')
mibBuilder.exportSymbols("OMNITRON-POE-MIB", ostPoePortPseEnable=ostPoePortPseEnable, ostPoePortHeartbeatInterval=ostPoePortHeartbeatInterval, ostPoeGlobalCfgPwrLimitationEnable=ostPoeGlobalCfgPwrLimitationEnable, ostPoePortHeartbeatEnable=ostPoePortHeartbeatEnable, ostPoePortPseStatus=ostPoePortPseStatus, ostPoePortHeartbeatIpAddress=ostPoePortHeartbeatIpAddress, PYSNMP_MODULE_ID=omnitronPoeMib, ostPoePortPseCurrentSupplied=ostPoePortPseCurrentSupplied, ostPoePortHeartbeatErrorDetection=ostPoePortHeartbeatErrorDetection, ostPoePortPdMode=ostPoePortPdMode, omnitronPoeMib=omnitronPoeMib, ostPoePortCfgEntry=ostPoePortCfgEntry, ostPoEPortHeartbeatDeferTime=ostPoEPortHeartbeatDeferTime, ostPoePortHeartbeatNumberRestarts=ostPoePortHeartbeatNumberRestarts, ostPoePortHeartbeatErrorAction=ostPoePortHeartbeatErrorAction, ostPoePortCfgIndex=ostPoePortCfgIndex, ostPoePortPseVoltageSupplied=ostPoePortPseVoltageSupplied, ostPoePortPse60wMode=ostPoePortPse60wMode, ostPoEPortHeartbeatStatus=ostPoEPortHeartbeatStatus, ostPoeGroup=ostPoeGroup, ostPoeGroups=ostPoeGroups, ostPoePortCfgTable=ostPoePortCfgTable, ostPoeCompliance=ostPoeCompliance, ostPoeGlobalCfgTotalPwr=ostPoeGlobalCfgTotalPwr, ostPoeGlobalCfgTable=ostPoeGlobalCfgTable, ostPoeCompliances=ostPoeCompliances)
