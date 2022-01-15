#
# PySNMP MIB module CTMMIBCUSTOM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ctm/CTMMIBCUSTOM
# Produced by pysmi-1.1.8 at Sat Jan 15 17:58:16 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Integer32, Counter32, Gauge32, MibIdentifier, Bits, ObjectIdentity, NotificationType, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lastmilegear = MibIdentifier((1, 3, 6, 1, 4, 1, 25868))
mibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25868, 1))
version = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('mandatory')
site = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: site.setStatus('mandatory')
lastIP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastIP.setStatus('mandatory')
lastTime = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastTime.setStatus('mandatory')
nSats = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nSats.setStatus('mandatory')
pwrP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrP.setStatus('mandatory')
pwrS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrS.setStatus('mandatory')
cbTrip = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbTrip.setStatus('mandatory')
tempC = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempC.setStatus('mandatory')
voltsM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsM1.setStatus('mandatory')
voltsM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsM2.setStatus('mandatory')
portOnM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOnM.setStatus('mandatory')
portSyncM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSyncM.setStatus('mandatory')
portPwrM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM1.setStatus('mandatory')
portPwrM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM2.setStatus('mandatory')
portPwrM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM3.setStatus('mandatory')
portPwrM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM4.setStatus('mandatory')
portPwrM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM5.setStatus('mandatory')
portPwrM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM6.setStatus('mandatory')
portPwrM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM7.setStatus('mandatory')
portPwrM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrM8.setStatus('mandatory')
pwrSP = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSP.setStatus('mandatory')
pwrSS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwrSS.setStatus('mandatory')
voltsS1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsS1.setStatus('mandatory')
voltsS2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltsS2.setStatus('mandatory')
portOnS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 29), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOnS.setStatus('mandatory')
portSyncS = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 30), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSyncS.setStatus('mandatory')
portPwrS1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 31), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS1.setStatus('mandatory')
portPwrS2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS2.setStatus('mandatory')
portPwrS3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS3.setStatus('mandatory')
portPwrS4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS4.setStatus('mandatory')
portPwrS5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS5.setStatus('mandatory')
portPwrS6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS6.setStatus('mandatory')
portPwrS7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 37), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS7.setStatus('mandatory')
portPwrS8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 38), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portPwrS8.setStatus('mandatory')
modeReqM = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 39), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modeReqM.setStatus('mandatory')
trpCntGM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM1.setStatus('mandatory')
trpCntGM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 46), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM2.setStatus('mandatory')
trpCntGM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 47), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM3.setStatus('mandatory')
trpCntGM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 48), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM4.setStatus('mandatory')
trpCntGM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 49), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM5.setStatus('mandatory')
trpCntGM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM6.setStatus('mandatory')
trpCntGM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM7.setStatus('mandatory')
trpCntGM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntGM8.setStatus('mandatory')
trpCntBM1 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM1.setStatus('mandatory')
trpCntBM2 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM2.setStatus('mandatory')
trpCntBM3 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM3.setStatus('mandatory')
trpCntBM4 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM4.setStatus('mandatory')
trpCntBM5 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM5.setStatus('mandatory')
trpCntBM6 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM6.setStatus('mandatory')
trpCntBM7 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 59), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM7.setStatus('mandatory')
trpCntBM8 = MibScalar((1, 3, 6, 1, 4, 1, 25868, 1, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpCntBM8.setStatus('mandatory')
lostEthernetConnection = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,0))
masterPrimayPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,1))
masterSecondaryPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,2))
gpsSignalLost = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,3))
masterTempatureError = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,4))
masterCircuitBreakerTripCode = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,5))
loginFailedAttempt = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,6))
settingsChanged = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,7))
masterPrimaryPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,10))
masterSecondaryPowerOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,20))
gpsSignalOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,30))
tempatureOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,40))
circuitBreakersOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,50))
masterAutoRestartCBCompletedOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,52))
loginOK = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,60))
resetComplete = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,80))
ethernetConnectionRestored = NotificationType((1, 3, 6, 1, 4, 1, 25868, 1) + (0,99))
mibBuilder.exportSymbols("CTMMIBCUSTOM", masterCircuitBreakerTripCode=masterCircuitBreakerTripCode, lastTime=lastTime, masterAutoRestartCBCompletedOK=masterAutoRestartCBCompletedOK, portPwrM1=portPwrM1, tempatureOK=tempatureOK, gpsSignalOK=gpsSignalOK, mibObjects=mibObjects, modeReqM=modeReqM, portPwrM3=portPwrM3, voltsM1=voltsM1, portPwrM5=portPwrM5, portSyncS=portSyncS, voltsS1=voltsS1, pwrP=pwrP, masterPrimaryPowerOK=masterPrimaryPowerOK, loginFailedAttempt=loginFailedAttempt, lastIP=lastIP, trpCntGM4=trpCntGM4, resetComplete=resetComplete, portPwrS3=portPwrS3, masterSecondaryPowerOK=masterSecondaryPowerOK, loginOK=loginOK, portPwrS8=portPwrS8, trpCntBM4=trpCntBM4, trpCntBM8=trpCntBM8, portPwrM8=portPwrM8, masterTempatureError=masterTempatureError, portPwrS1=portPwrS1, portPwrM6=portPwrM6, trpCntBM1=trpCntBM1, portPwrS7=portPwrS7, portPwrM2=portPwrM2, portPwrM7=portPwrM7, trpCntGM8=trpCntGM8, pwrS=pwrS, trpCntGM3=trpCntGM3, trpCntBM6=trpCntBM6, portPwrS6=portPwrS6, lostEthernetConnection=lostEthernetConnection, portSyncM=portSyncM, tempC=tempC, masterSecondaryPowerLost=masterSecondaryPowerLost, circuitBreakersOK=circuitBreakersOK, nSats=nSats, trpCntBM7=trpCntBM7, trpCntGM7=trpCntGM7, trpCntBM2=trpCntBM2, version=version, cbTrip=cbTrip, ethernetConnectionRestored=ethernetConnectionRestored, masterPrimayPowerLost=masterPrimayPowerLost, portOnM=portOnM, pwrSP=pwrSP, pwrSS=pwrSS, portPwrS5=portPwrS5, lastmilegear=lastmilegear, portPwrS4=portPwrS4, trpCntGM5=trpCntGM5, gpsSignalLost=gpsSignalLost, site=site, trpCntGM6=trpCntGM6, trpCntGM1=trpCntGM1, portPwrS2=portPwrS2, voltsS2=voltsS2, trpCntBM3=trpCntBM3, voltsM2=voltsM2, trpCntBM5=trpCntBM5, portPwrM4=portPwrM4, portOnS=portOnS, trpCntGM2=trpCntGM2, settingsChanged=settingsChanged)
