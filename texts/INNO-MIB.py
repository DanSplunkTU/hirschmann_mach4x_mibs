#
# PySNMP MIB module INNO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/innovaphone/INNO-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:27:48 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, TimeTicks, ModuleIdentity, Integer32, NotificationType, Bits, ObjectIdentity, Gauge32, Counter64, Counter32, Unsigned32, iso, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "TimeTicks", "ModuleIdentity", "Integer32", "NotificationType", "Bits", "ObjectIdentity", "Gauge32", "Counter64", "Counter32", "Unsigned32", "iso", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

innovaphone = MibIdentifier((1, 3, 6, 1, 4, 1, 6666))
isdn = MibIdentifier((1, 3, 6, 1, 4, 1, 6666, 1))
l2Table = MibTable((1, 3, 6, 1, 4, 1, 6666, 1, 1), )
if mibBuilder.loadTexts: l2Table.setStatus('mandatory')
if mibBuilder.loadTexts: l2Table.setDescription('ISDN layer2 table')
l2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 6666, 1, 1, 1), ).setIndexNames((0, "INNO-MIB", "l2Label"))
if mibBuilder.loadTexts: l2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: l2Entry.setDescription('Layer 2 Entry')
l2Label = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2Label.setStatus('mandatory')
if mibBuilder.loadTexts: l2Label.setDescription('Name of this Layer 2 instance')
l2State = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2State.setStatus('mandatory')
if mibBuilder.loadTexts: l2State.setDescription('Indication whether the LAPD layer is active')
l2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("te", 1), ("nt", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l2Mode.setStatus('mandatory')
if mibBuilder.loadTexts: l2Mode.setDescription('Interface mode, either NT or TE')
l1Label = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1Label.setStatus('mandatory')
if mibBuilder.loadTexts: l1Label.setDescription('Name of Layer 1 (physical) instance this Layer 2\n             instance is working on')
l1PriTable = MibTable((1, 3, 6, 1, 4, 1, 6666, 1, 2), )
if mibBuilder.loadTexts: l1PriTable.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriTable.setDescription('Layer1 table (primary rate interface)')
l1PriEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1), ).setIndexNames((0, "INNO-MIB", "l1PriLabel"))
if mibBuilder.loadTexts: l1PriEntry.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriEntry.setDescription('Layer 1 Entry (primary rate interface)')
l1PriLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriLabel.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriLabel.setDescription('Name of this Layer 1 instance')
l1PriState = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriState.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriState.setDescription('Indication whether the physical layer is active')
l1PriErrCrc4 = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrCrc4.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrCrc4.setDescription('The CRC4 check of a received submultiframe failed.')
l1PriErrRemAlarmInd = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrRemAlarmInd.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrRemAlarmInd.setDescription('Remote Alarm')
l1PriErrSigLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrSigLoss.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrSigLoss.setDescription('Loss of signal')
l1PriErrAlarmInd = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrAlarmInd.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrAlarmInd.setDescription('Alarm Indication Signal')
l1PriErrFrameAlignmentTOut = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrFrameAlignmentTOut.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrFrameAlignmentTOut.setDescription('Receive Time Out 400 msec')
l1PriErrFrameAlignmentLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrFrameAlignmentLoss.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrFrameAlignmentLoss.setDescription('Loss of Frame Alignment')
l1PriErrSlip = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1PriErrSlip.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriErrSlip.setDescription('Receive SLIP detected')
l1PriTest = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noTest", 0), ("simAlarm", 1), ("resetAlarms", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l1PriTest.setStatus('mandatory')
if mibBuilder.loadTexts: l1PriTest.setDescription('Triggers,resets some hardware alarm counters ')
l1BriTable = MibTable((1, 3, 6, 1, 4, 1, 6666, 1, 3), )
if mibBuilder.loadTexts: l1BriTable.setStatus('mandatory')
if mibBuilder.loadTexts: l1BriTable.setDescription('Layer1 table (basic rate interface)')
l1BriEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6666, 1, 3, 1), ).setIndexNames((0, "INNO-MIB", "l1BriLabel"))
if mibBuilder.loadTexts: l1BriEntry.setStatus('mandatory')
if mibBuilder.loadTexts: l1BriEntry.setDescription('Layer 1 Entry (basic rate rate interface)')
l1BriLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1BriLabel.setStatus('mandatory')
if mibBuilder.loadTexts: l1BriLabel.setDescription('Name of this Layer 1 instance')
l1BriState = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l1BriState.setStatus('mandatory')
if mibBuilder.loadTexts: l1BriState.setDescription('Indication whether the physical layer is active')
l3Table = MibTable((1, 3, 6, 1, 4, 1, 6666, 1, 4), )
if mibBuilder.loadTexts: l3Table.setStatus('mandatory')
if mibBuilder.loadTexts: l3Table.setDescription('Layer3 table')
l3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1), ).setIndexNames((0, "INNO-MIB", "l3Label"))
if mibBuilder.loadTexts: l3Entry.setStatus('mandatory')
if mibBuilder.loadTexts: l3Entry.setDescription('Layer 3 Entry')
l3Label = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3Label.setStatus('mandatory')
if mibBuilder.loadTexts: l3Label.setDescription('Name of this Layer 3 instance')
l3Protocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 23))).clone(namedValues=NamedValues(("none", 0), ("other", 1), ("etsi", 3), ("qsig", 23)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3Protocol.setStatus('mandatory')
if mibBuilder.loadTexts: l3Protocol.setDescription('The Isdn signalling protocol on this interface')
l3NumBchan = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3NumBchan.setStatus('mandatory')
if mibBuilder.loadTexts: l3NumBchan.setDescription('Number of B-channels available')
l3NumBchanActive = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3NumBchanActive.setStatus('mandatory')
if mibBuilder.loadTexts: l3NumBchanActive.setDescription('Number of B-channels currently active.\n            May also be understood as number of calls\n            currently active on this interface.')
l3CallsBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: l3CallsBoot.setStatus('mandatory')
if mibBuilder.loadTexts: l3CallsBoot.setDescription('Accumulated Number of Calls on this interface\n            since last Boot')
gateway = MibIdentifier((1, 3, 6, 1, 4, 1, 6666, 2))
gatekeeper = MibIdentifier((1, 3, 6, 1, 4, 1, 6666, 2, 1))
voiceIfTable = MibTable((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1), )
if mibBuilder.loadTexts: voiceIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfTable.setDescription('Voice Interfaces Table. Features either\n            physical interfaces or aliases.')
voiceIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1), ).setIndexNames((0, "INNO-MIB", "voiceIfIndex"), (0, "INNO-MIB", "voiceIfAliasIndex"))
if mibBuilder.loadTexts: voiceIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfEntry.setDescription('Voice Interfaces Entry.Features either\n            physical interfaces or aliases.')
voiceIfGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfGwName.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfGwName.setDescription('Only of interest for aliases to show at which GWxx\n            an alias has been/will be registered')
voiceIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unkown", 0), ("if", 1), ("ep", 2), ("gk", 3), ("gw", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfType.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfType.setDescription('The type of the interface')
voiceIfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfAddr.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfAddr.setDescription('ip address, only of interest if interface state \n             is up')
voiceIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfState.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfState.setDescription('Interface state')
voiceIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfNumber.setDescription('The E.164 number registered by this interface')
voiceIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfName.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfName.setDescription('The H.323 Name registered by this interface')
voiceIfProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfProduct.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfProduct.setDescription('If available the description of the registering\n            product')
voiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: voiceIfIndex.setDescription('Increasing index of an interface,\n            utilized as first suboid of entry index.')
voiceIfAliasIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceIfAliasIndex.setStatus('optional')
if mibBuilder.loadTexts: voiceIfAliasIndex.setDescription('If interface is an alias, this is the\n        increasing index of alias at an interface. \n        Otherwise -1 will be returned.\n        Utilized as second suboid of entry index.')
trapDummyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 6666, 3))
trapDisplayStringParm = MibScalar((1, 3, 6, 1, 4, 1, 6666, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDisplayStringParm.setStatus('mandatory')
if mibBuilder.loadTexts: trapDisplayStringParm.setDescription("This variable doesn't exist. Its purpose is to\n             be syntactically referenced as a variable within \n             a trap.")
trapIntegerParm = MibScalar((1, 3, 6, 1, 4, 1, 6666, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIntegerParm.setStatus('mandatory')
if mibBuilder.loadTexts: trapIntegerParm.setDescription("This variable doesn't exist. Its purpose is to\n             be syntactically referenced as a variable within \n             a trap.")
trapGaugeParm = MibScalar((1, 3, 6, 1, 4, 1, 6666, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapGaugeParm.setStatus('mandatory')
if mibBuilder.loadTexts: trapGaugeParm.setDescription("This variable doesn't exist. Its purpose is to\n             be syntactically referenced as a variable within \n             a trap.")
innoColdStart = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,0))
if mibBuilder.loadTexts: innoColdStart.setDescription('An unexpected restart happened.')
innoWarmStart = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,1))
if mibBuilder.loadTexts: innoWarmStart.setDescription('The device has been reset administratively.')
innoLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: innoLinkDown.setDescription('An interface link went down (PPP).')
innoLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: innoLinkUp.setDescription('An interface link went up.')
innoAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,4))
if mibBuilder.loadTexts: innoAuthenticationFailure.setDescription('An Snmp PDU with a wrong community string has\n        been received.')
innoIsdnFailure = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,5)).setObjects(("INNO-MIB", "trapDisplayStringParm"), ("INNO-MIB", "trapIntegerParm"))
if mibBuilder.loadTexts: innoIsdnFailure.setDescription('Obsoleted: This SNMP trap is no longer necessary. Meanwhile it is covered more consistently by innoDiagAlarm and innoDiagAlarmClear.\n         Removed from on v9hf16.')
innoDiagAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,6)).setObjects(("INNO-MIB", "trapGaugeParm"), ("INNO-MIB", "trapDisplayStringParm"), ("INNO-MIB", "trapGaugeParm"), ("INNO-MIB", "trapDisplayStringParm"))
if mibBuilder.loadTexts: innoDiagAlarm.setDescription('This trap corresponds to an alarm under Administration/Diagnostics/Alarms')
innoDiagAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 6666) + (0,7)).setObjects(("INNO-MIB", "trapGaugeParm"), ("INNO-MIB", "trapDisplayStringParm"))
if mibBuilder.loadTexts: innoDiagAlarmClear.setDescription('This trap corresponds to an alarm clearing under Administration/Diagnostics/Alarms')
mibBuilder.exportSymbols("INNO-MIB", l1PriTable=l1PriTable, innoLinkDown=innoLinkDown, l1BriTable=l1BriTable, l2State=l2State, l2Mode=l2Mode, l1BriEntry=l1BriEntry, voiceIfNumber=voiceIfNumber, innovaphone=innovaphone, l1PriErrCrc4=l1PriErrCrc4, DisplayString=DisplayString, l1PriTest=l1PriTest, l3Entry=l3Entry, l1PriEntry=l1PriEntry, l1PriErrAlarmInd=l1PriErrAlarmInd, l3Label=l3Label, l1PriErrSlip=l1PriErrSlip, l3NumBchan=l3NumBchan, l3Protocol=l3Protocol, voiceIfState=voiceIfState, trapDisplayStringParm=trapDisplayStringParm, l1PriErrFrameAlignmentLoss=l1PriErrFrameAlignmentLoss, l1BriState=l1BriState, l3NumBchanActive=l3NumBchanActive, trapDummyGroup=trapDummyGroup, voiceIfAliasIndex=voiceIfAliasIndex, innoAuthenticationFailure=innoAuthenticationFailure, l3CallsBoot=l3CallsBoot, innoLinkUp=innoLinkUp, innoIsdnFailure=innoIsdnFailure, trapIntegerParm=trapIntegerParm, gateway=gateway, l2Table=l2Table, gatekeeper=gatekeeper, voiceIfEntry=voiceIfEntry, innoColdStart=innoColdStart, isdn=isdn, voiceIfIndex=voiceIfIndex, voiceIfName=voiceIfName, innoDiagAlarm=innoDiagAlarm, l1Label=l1Label, l1BriLabel=l1BriLabel, innoDiagAlarmClear=innoDiagAlarmClear, l1PriErrFrameAlignmentTOut=l1PriErrFrameAlignmentTOut, l1PriErrRemAlarmInd=l1PriErrRemAlarmInd, l2Label=l2Label, innoWarmStart=innoWarmStart, voiceIfGwName=voiceIfGwName, voiceIfAddr=voiceIfAddr, l1PriErrSigLoss=l1PriErrSigLoss, l3Table=l3Table, l2Entry=l2Entry, l1PriLabel=l1PriLabel, trapGaugeParm=trapGaugeParm, voiceIfProduct=voiceIfProduct, voiceIfType=voiceIfType, voiceIfTable=voiceIfTable, l1PriState=l1PriState)
