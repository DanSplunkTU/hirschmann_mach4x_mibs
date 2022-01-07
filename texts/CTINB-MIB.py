#
# PySNMP MIB module CTINB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTINB-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:05:38 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctINBinfo, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctINBinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, Gauge32, MibIdentifier, TimeTicks, Unsigned32, ModuleIdentity, Counter32, ObjectIdentity, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32", "ObjectIdentity", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
inbMonarchSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1))
inbMonarchSystemTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1), )
if mibBuilder.loadTexts: inbMonarchSystemTable.setStatus('mandatory')
inbMonarchSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbMonarchINB"))
if mibBuilder.loadTexts: inbMonarchSystemEntry.setStatus('mandatory')
inbMonarchSystemINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSystemINB.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchSystemINB.setDescription("Two physical INB's may exist on a module. This\n                    object distinquishes which INB, INB-A or INB-B.")
inbMonarchStatusTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchStatusTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchStatusTimeStamp.setDescription('This object represents the value of sysUptime when\n                     the Monarch last changed.')
inbMonarchBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchBandwidth.setDescription('The bandwidth of this INB in Megabits.')
inbMonarchTDMSlotMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("userPolicy", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotMode.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchTDMSlotMode.setDescription('The automatic TDM mode overides any preset TDM\n                     allocation. All boards get an equal number of \n                     pre-allocated TDM slots, adding up to 100% of total\n                     INB bandwidth, and have Round Robin enabled. The\n                     automatic mode will, in effect, provide each board\n                     with a 1/(number of boards) minimum guarantee\n                     INB bandwidth.\n \n                     The userPolicy mode will have the per board policy\n                     enforced. Each board will have a level of service\n                     (TDM slots, Round Robin arbitration from the \n                     inbMonarchTable) associated with it to take effect\n                     when this object is set to user_policy. Newly\n                     inserted boards will default to Round Robin and\n                     share the remaining fixed INB bandwidth\n                     (inbMonarchTDMSlotTotal - inbMonarchTDMSlotActual).')
inbMonarchTDMSlotTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchTDMSlotTotal.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchTDMSlotTotal.setDescription('This object represents the total possible number of INB\n                     backplane TDM slots.')
inbMonarchSystemTDMSlotActual = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSystemTDMSlotActual.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchSystemTDMSlotActual.setDescription('This object represents the total number of allocated INB\n                     backplane TDM slots. This is the sum of all instances of\n                     inbMonarchTDMSlotRequest in userPolicy mode. In automatic\n                     mode this number would represent the number of inserted\n                     boards.')
inbMonarchTDMSlotbandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchTDMSlotbandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchTDMSlotbandwidth.setDescription('This object represents the bandwidth in bits that\n                     each slot represents on the backplane.')
inbMonarch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2))
inbMonarchTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1), )
if mibBuilder.loadTexts: inbMonarchTable.setStatus('mandatory')
inbMonarchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbMonarchSlot"), (0, "CTINB-MIB", "inbMonarchINB"))
if mibBuilder.loadTexts: inbMonarchEntry.setStatus('mandatory')
inbMonarchSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchSlot.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchSlot.setDescription('The slot number containing this module.')
inbMonarchINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchINB.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchINB.setDescription('Two physical INB interfaces may exist on a module. This\n                    object distinquishes which INB, INB-A or INB-B.')
inbMonarchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("standBy", 1), ("sysUndefined", 2), ("operational", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchStatus.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchStatus.setDescription('Application state of the monarch application on this\n                    module. Standby - indicates this module is not the\n                    monarch but can be. SysUndefined - indicates this\n                    module can not be monarch. Operational - says this\n                    module is the monarch. ')
inbMonarchLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("linkUp", 1), ("linkDown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchLinkStatus.setDescription('This object describes the state of the backplane. LinkUp\n                     is when this INB detects the clock on the backplane.\n                     LinkDown is when no backplane clock has been detected.')
inbMonarchLinkCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchLinkCapacity.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchLinkCapacity.setDescription('The bandwidth capacity of this board in Megabytes.')
inbMonarchTDMSlotRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotRequest.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchTDMSlotRequest.setDescription('This object is the number of fixed TDM slots requested\n                     for this board . NOTE: new request will take effect the\n                     next time the inbMonarchTDMSlotMode object is set to\n                     userPolicy. NOTE: this value has no meaning when the\n                     inbMonarchTDMSlotMode is automatic.')
inbMonarchTDMSlotActual = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inbMonarchTDMSlotActual.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchTDMSlotActual.setDescription('This object is the actual number of fixed TDM slots\n                     given to this board. In automatic mode, this value is the\n                     total number of slots divided by the number of inserted\n                     boards, in userPolicy mode, this reflects the\n                     inbMonarchTDMSlotRequest value at the last time the\n                     chassis entered userPolicy mode.')
inbMonarchRoundRobinControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbMonarchRoundRobinControl.setStatus('mandatory')
if mibBuilder.loadTexts: inbMonarchRoundRobinControl.setDescription('This object enables or disable this INB the ability to\n                     participate in the Round Robin arbitration phase.')
inbStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3))
inbStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1), )
if mibBuilder.loadTexts: inbStatsTable.setStatus('mandatory')
inbStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1), ).setIndexNames((0, "CTINB-MIB", "inbStatsSlot"), (0, "CTINB-MIB", "inbStatsINB"))
if mibBuilder.loadTexts: inbStatsEntry.setStatus('mandatory')
inbStatsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsSlot.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsSlot.setDescription('The slot number containing this module.')
inbStatsINB = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inbA", 1), ("inbB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsINB.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsINB.setDescription('Two physical INB interfaces may exist on a module. This\n                    object distinquishes which INB, INB-A or INB-B.')
inbStatsIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsIfindex.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsIfindex.setDescription('The interface number of the INB. The interface \n                     identified by a particular value of this\n                     object is the same interface as identified by the\n                     same value of the ifIndex object defined in RFC 1213.')
inbStatsUniCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsUniCastCells.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsUniCastCells.setDescription('Number of UniCast INB cells received from the backplane.')
inbStatsMultiCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsMultiCastCells.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsMultiCastCells.setDescription('Number of multi-cast INB cells received from the backplane.')
inbStatsBroadCastCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsBroadCastCells.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsBroadCastCells.setDescription('Number of broadcast INB cells received from the backplane.')
inbStatsXmitCells = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsXmitCells.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsXmitCells.setDescription('Number of INB cells transmitted to the backplane.')
inbStatsRecvSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsRecvSeqErrs.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsRecvSeqErrs.setDescription('Number of pkts with sequence errors received from\n                     the backplane.')
inbStatsRecvChksumErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsRecvChksumErrs.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsRecvChksumErrs.setDescription('Number of pkts with checksum errors received from\n                     the backplane.')
inbStatsxmitToFps = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsxmitToFps.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsxmitToFps.setDescription('Number of transmit errors to FPS.')
inbStatsToFpsDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToFpsDrops.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsToFpsDrops.setDescription('INBC receive fifo full count. This represents the\n                     number of cells that were not forwarded to the FPS.')
inbStatsFromInbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsFromInbErrs.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsFromInbErrs.setDescription('Number of INB receive errors from the backplane. This\n                     includes FPSC xmit errors(inbStatsxmitToFps), INBC\n                     receive sequence errors (inbStatsRecvSeqErrs)\n                     and INBC checksum errors(inbStatsRecvChksumErrs).')
inbStatsToINBDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToINBDrops.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsToINBDrops.setDescription('Number of FPSC recv frame drop count. This represents\n                     the number of frames that were not sent out on the INB\n                     backplane.')
inbStatsToInbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inbStatsToInbErrs.setStatus('mandatory')
if mibBuilder.loadTexts: inbStatsToInbErrs.setDescription('Number of INB backplane transmit errors. This includes\n                     FPSC receive timeout errors')
mibBuilder.exportSymbols("CTINB-MIB", inbStatsRecvSeqErrs=inbStatsRecvSeqErrs, inbMonarch=inbMonarch, inbMonarchTDMSlotActual=inbMonarchTDMSlotActual, inbStatsToInbErrs=inbStatsToInbErrs, inbStatsUniCastCells=inbStatsUniCastCells, inbMonarchSystemTable=inbMonarchSystemTable, inbStatsFromInbErrs=inbStatsFromInbErrs, inbStatsIfindex=inbStatsIfindex, inbMonarchTDMSlotRequest=inbMonarchTDMSlotRequest, inbMonarchLinkCapacity=inbMonarchLinkCapacity, inbMonarchStatusTimeStamp=inbMonarchStatusTimeStamp, inbMonarchTDMSlotMode=inbMonarchTDMSlotMode, inbMonarchTDMSlotTotal=inbMonarchTDMSlotTotal, inbMonarchSystemTDMSlotActual=inbMonarchSystemTDMSlotActual, inbMonarchEntry=inbMonarchEntry, inbMonarchSlot=inbMonarchSlot, inbMonarchStatus=inbMonarchStatus, inbStatsEntry=inbStatsEntry, inbMonarchSystemEntry=inbMonarchSystemEntry, inbStatsXmitCells=inbStatsXmitCells, inbStatsSlot=inbStatsSlot, inbMonarchLinkStatus=inbMonarchLinkStatus, inbMonarchRoundRobinControl=inbMonarchRoundRobinControl, inbStatsRecvChksumErrs=inbStatsRecvChksumErrs, inbMonarchTable=inbMonarchTable, inbMonarchSystem=inbMonarchSystem, inbStatsMultiCastCells=inbStatsMultiCastCells, inbStatsToINBDrops=inbStatsToINBDrops, inbMonarchSystemINB=inbMonarchSystemINB, inbStatsBroadCastCells=inbStatsBroadCastCells, inbStatsINB=inbStatsINB, inbMonarchBandwidth=inbMonarchBandwidth, inbMonarchTDMSlotbandwidth=inbMonarchTDMSlotbandwidth, inbMonarchINB=inbMonarchINB, inbStatsToFpsDrops=inbStatsToFpsDrops, inbStats=inbStats, inbStatsxmitToFps=inbStatsxmitToFps, inbStatsTable=inbStatsTable)
