#
# PySNMP MIB module STXN-GLOBALREGISTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/STXN-GLOBALREGISTER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:50:45 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Counter32, MibIdentifier, IpAddress, Unsigned32, Counter64, enterprises, Bits, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Counter32", "MibIdentifier", "IpAddress", "Unsigned32", "Counter64", "enterprises", "Bits", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stxnGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 6, 1))
stxnGlobalRegModule.setRevisions(('2014-01-21 03:58', '2011-11-28 00:07', '2011-03-14 01:19', '2009-07-23 04:15', '2009-04-16 23:58', '2004-02-20 00:55', '2003-01-29 03:31', '2002-11-28 23:58', '2002-10-08 19:35', '2002-09-03 23:15', '2001-11-15 01:10', '2001-03-14 20:41', '2001-02-13 20:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stxnGlobalRegModule.setRevisionsDescriptions(('Added sub-module branches for Aviat products.', 'Added the registration for stxnProductOIDs branch.', 'Added the registration for aviatModules, aviatEvents and\n                 aviatProducts branches.  Refer to MDR #320.', 'Added the registration for stxnEfficientSiteControllerUnit\n                 branch.  Refer to MDR #288.', 'Added the registration for EfficientSite products and new\n                 product event branches.  Refer to MDR #273.', 'Added the registration for ProVision products and new\n                 product event branches.', 'Added the registration for UNITY products branch.', 'Added the registration for AOU and CTU product branches.', 'Added the registration for AOU and CTU events.', "As part of the clean up exercise for the STXN Generic\n                 MIB modules that have not been 'released', the stxnGeneric\n                 branch has been re-registered under a different number.\n                 It used to be dmc 3 and now it is dmc 8.", 'Added registration for event OIDs.', 'Updated following the Common MIB Review held in Wellington.', 'Initial version.',))
if mibBuilder.loadTexts: stxnGlobalRegModule.setLastUpdated('201401210358Z')
if mibBuilder.loadTexts: stxnGlobalRegModule.setOrganization('Aviat Networks')
if mibBuilder.loadTexts: stxnGlobalRegModule.setContactInfo('Aviat Networks\n                         Customer Service\n\n                         Postal: 5200 Great America Parkway\n                                 Santa Clara\n                                 California 95054\n                                 United States of America\n\n                         Tel: 408 567 7000\n\n                         E-mail: mibsupport@aviatnet.com')
if mibBuilder.loadTexts: stxnGlobalRegModule.setDescription('This module defines the OID infrastructure under the DMC\n                 Enterprise MIB Branch.')
dmc = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509))
if mibBuilder.loadTexts: dmc.setStatus('current')
if mibBuilder.loadTexts: dmc.setDescription('The root of the OID sub-tree assigned to DMC Stratex\n                         Networks by the Internet Assigned Numbers Authority\n                         (IANA).')
dmcNet = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1))
if mibBuilder.loadTexts: dmcNet.setStatus('current')
if mibBuilder.loadTexts: dmcNet.setDescription('dmcNet branch.')
proxyAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 1))
if mibBuilder.loadTexts: proxyAgent.setStatus('current')
if mibBuilder.loadTexts: proxyAgent.setDescription('proxyAgent branch.')
nonsnmpRadio = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 2))
if mibBuilder.loadTexts: nonsnmpRadio.setStatus('current')
if mibBuilder.loadTexts: nonsnmpRadio.setDescription('nonsnmpRadio branch.')
snmpRadio = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 3))
if mibBuilder.loadTexts: snmpRadio.setStatus('current')
if mibBuilder.loadTexts: snmpRadio.setDescription('snmpRadio branch.')
dmcEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 4))
if mibBuilder.loadTexts: dmcEvents.setStatus('current')
if mibBuilder.loadTexts: dmcEvents.setDescription('dmcEvents branch.')
dmcSecurity = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 5))
if mibBuilder.loadTexts: dmcSecurity.setStatus('current')
if mibBuilder.loadTexts: dmcSecurity.setDescription('dmcSecurity branch.')
sp2Radio = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 3, 1))
if mibBuilder.loadTexts: sp2Radio.setStatus('current')
if mibBuilder.loadTexts: sp2Radio.setDescription('sp2Radio branch for the Spectrum II product.')
altium = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 1, 3, 2))
if mibBuilder.loadTexts: altium.setStatus('current')
if mibBuilder.loadTexts: altium.setDescription('altium branch for the Altium product.')
dmcModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 2))
if mibBuilder.loadTexts: dmcModules.setStatus('current')
if mibBuilder.loadTexts: dmcModules.setDescription('dmcModules branch.')
stxnEngineering = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 4))
if mibBuilder.loadTexts: stxnEngineering.setStatus('current')
if mibBuilder.loadTexts: stxnEngineering.setDescription('This sub-tree holds all the MIB modules developed for\n                         Engineering purposes within Harris Stratex Networks.')
stxnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5))
if mibBuilder.loadTexts: stxnProducts.setStatus('current')
if mibBuilder.loadTexts: stxnProducts.setDescription('This sub-tree holds all the MIB modules developed for\n                         specific products of Harris Stratex Networks.')
stxnLMCDR = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 1))
if mibBuilder.loadTexts: stxnLMCDR.setStatus('current')
if mibBuilder.loadTexts: stxnLMCDR.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Low / Medium Capacity Data Radio of Harris Stratex\n                         Networks.')
stxnAOU = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 2))
if mibBuilder.loadTexts: stxnAOU.setStatus('current')
if mibBuilder.loadTexts: stxnAOU.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Eclipse All Outdoor Unit (AOU) product of Harris\n                         Stratex Networks.')
stxnCTU = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 3))
if mibBuilder.loadTexts: stxnCTU.setStatus('current')
if mibBuilder.loadTexts: stxnCTU.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Eclipse Intelligent Node Unit (INU) product of\n                         Harris Stratex Networks.\n\n                         Note that the INU was previously known as CTU.')
stxnUNITY = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 4))
if mibBuilder.loadTexts: stxnUNITY.setStatus('current')
if mibBuilder.loadTexts: stxnUNITY.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Eclipse products of Harris Stratex Networks.\n\n                         Note that Eclipse was previously referred to as Unity.')
stxnProVision = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 5))
if mibBuilder.loadTexts: stxnProVision.setStatus('current')
if mibBuilder.loadTexts: stxnProVision.setDescription('This sub-tree holds all the MIB modules developed for\n                         the ProVision product of Harris Stratex Networks.')
stxnEfficientSite = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 6))
if mibBuilder.loadTexts: stxnEfficientSite.setStatus('current')
if mibBuilder.loadTexts: stxnEfficientSite.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Efficient Site products of Harris Stratex\n                         Networks.')
stxnEfficientSiteControllerUnit = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 6, 1))
if mibBuilder.loadTexts: stxnEfficientSiteControllerUnit.setStatus('current')
if mibBuilder.loadTexts: stxnEfficientSiteControllerUnit.setDescription('This sub-tree holds all the MIB modules developed for\n                         the Efficient Site Controller Unit - partnership\n                         product with Asentria.\n\n                         Note that the MIB definitions below this node are\n                         managed and controlled by Asentria.')
stxnProductOIDs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 5, 10))
if mibBuilder.loadTexts: stxnProductOIDs.setStatus('current')
if mibBuilder.loadTexts: stxnProductOIDs.setDescription('This sub-tree holds the object identifiers that are\n                         assigned to Eclipse products.')
stxnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 6))
if mibBuilder.loadTexts: stxnModules.setStatus('current')
if mibBuilder.loadTexts: stxnModules.setDescription('This sub-tree holds all MIB modules that are\n                         registered for STXN under the DMC tree.')
stxnEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7))
if mibBuilder.loadTexts: stxnEvents.setStatus('current')
if mibBuilder.loadTexts: stxnEvents.setDescription('This sub-tree holds all Event Definitions registered\n                         for STXN under the DMC tree.')
stxnGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 8))
if mibBuilder.loadTexts: stxnGeneric.setStatus('current')
if mibBuilder.loadTexts: stxnGeneric.setDescription('This sub-tree holds all the reusable generic MIB\n                         modules for the Harris Stratex Networks product range.')
aviatModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 9))
if mibBuilder.loadTexts: aviatModules.setStatus('current')
if mibBuilder.loadTexts: aviatModules.setDescription('This sub-tree holds all MIB modules that are\n                         registered for Aviat under the DMC tree.')
aviatAfModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1000))
if mibBuilder.loadTexts: aviatAfModules.setStatus('current')
if mibBuilder.loadTexts: aviatAfModules.setDescription('This sub-tree holds a group of MIBs that are common to\n                         a specific functional area for Aviat products.')
aviatAaModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1001))
if mibBuilder.loadTexts: aviatAaModules.setStatus('current')
if mibBuilder.loadTexts: aviatAaModules.setDescription('This sub-tree holds a group of MIBs that are common to\n                         a specific functional area for Aviat products.')
aviatAlModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1002))
if mibBuilder.loadTexts: aviatAlModules.setStatus('current')
if mibBuilder.loadTexts: aviatAlModules.setDescription('This sub-tree holds a group of MIBs that are common to\n                         a specific functional area for Aviat products.')
aviatAmModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 1003))
if mibBuilder.loadTexts: aviatAmModules.setStatus('current')
if mibBuilder.loadTexts: aviatAmModules.setDescription('This sub-tree holds a group of MIBs that are common to\n                         a specific functional area for Aviat products.')
aviatEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 10))
if mibBuilder.loadTexts: aviatEvents.setStatus('current')
if mibBuilder.loadTexts: aviatEvents.setDescription('This sub-tree holds all Event Definitions registered\n                         for Aviat under the DMC tree.')
aviatProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 11))
if mibBuilder.loadTexts: aviatProducts.setStatus('current')
if mibBuilder.loadTexts: aviatProducts.setDescription('This sub-tree contains objects to describe Aviat\n                         Networks products.')
stxnOvationEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7, 1))
if mibBuilder.loadTexts: stxnOvationEvents.setStatus('current')
if mibBuilder.loadTexts: stxnOvationEvents.setDescription('Event Definition.')
stxnUnityAOUEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7, 2))
if mibBuilder.loadTexts: stxnUnityAOUEvents.setStatus('current')
if mibBuilder.loadTexts: stxnUnityAOUEvents.setDescription('Event Definition.')
stxnUnityCTUEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7, 3))
if mibBuilder.loadTexts: stxnUnityCTUEvents.setStatus('current')
if mibBuilder.loadTexts: stxnUnityCTUEvents.setDescription('Event Definition.')
stxnUnityIDUEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7, 4))
if mibBuilder.loadTexts: stxnUnityIDUEvents.setStatus('current')
if mibBuilder.loadTexts: stxnUnityIDUEvents.setDescription('Event Definition.')
stxnEfficientSiteEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 2509, 7, 5))
if mibBuilder.loadTexts: stxnEfficientSiteEvents.setStatus('current')
if mibBuilder.loadTexts: stxnEfficientSiteEvents.setDescription('Event Definition.')
mibBuilder.exportSymbols("STXN-GLOBALREGISTER-MIB", stxnEfficientSiteControllerUnit=stxnEfficientSiteControllerUnit, dmcSecurity=dmcSecurity, aviatModules=aviatModules, stxnEngineering=stxnEngineering, dmc=dmc, altium=altium, stxnCTU=stxnCTU, sp2Radio=sp2Radio, snmpRadio=snmpRadio, stxnUNITY=stxnUNITY, stxnEfficientSiteEvents=stxnEfficientSiteEvents, aviatProducts=aviatProducts, stxnUnityCTUEvents=stxnUnityCTUEvents, stxnEfficientSite=stxnEfficientSite, stxnGeneric=stxnGeneric, stxnProVision=stxnProVision, aviatAmModules=aviatAmModules, aviatEvents=aviatEvents, dmcModules=dmcModules, stxnEvents=stxnEvents, stxnModules=stxnModules, nonsnmpRadio=nonsnmpRadio, stxnAOU=stxnAOU, dmcNet=dmcNet, proxyAgent=proxyAgent, aviatAlModules=aviatAlModules, stxnLMCDR=stxnLMCDR, stxnOvationEvents=stxnOvationEvents, aviatAfModules=aviatAfModules, stxnProductOIDs=stxnProductOIDs, stxnGlobalRegModule=stxnGlobalRegModule, stxnUnityIDUEvents=stxnUnityIDUEvents, aviatAaModules=aviatAaModules, stxnUnityAOUEvents=stxnUnityAOUEvents, stxnProducts=stxnProducts, PYSNMP_MODULE_ID=stxnGlobalRegModule, dmcEvents=dmcEvents)
