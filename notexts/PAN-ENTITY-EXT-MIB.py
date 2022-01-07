#
# PySNMP MIB module PAN-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-ENTITY-EXT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:21:54 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Bits, TimeTicks, Counter64, iso, Unsigned32, ObjectIdentity, ModuleIdentity, MibIdentifier, Gauge32, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "Counter64", "iso", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panEntityMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7))
panEntityMIBModule.setRevisions(('2012-11-05 11:06',))
if mibBuilder.loadTexts: panEntityMIBModule.setLastUpdated('201211051106Z')
if mibBuilder.loadTexts: panEntityMIBModule.setOrganization('Palo Alto Networks')
panEntityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1))
panEntityMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2))
panEntityChassisGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1))
if mibBuilder.loadTexts: panEntityChassisGroup.setStatus('current')
panEntityFRUModuleGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2))
if mibBuilder.loadTexts: panEntityFRUModuleGroup.setStatus('current')
panEntityFanTrayGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3))
if mibBuilder.loadTexts: panEntityFanTrayGroup.setStatus('current')
panEntityPowerSupplyGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4))
if mibBuilder.loadTexts: panEntityPowerSupplyGroup.setStatus('current')
panEntityTotalPowerAvail = MibScalar((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntityTotalPowerAvail.setStatus('current')
panEntityTotalPowerUsed = MibScalar((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntityTotalPowerUsed.setStatus('current')
panEntityFRUModuleTable = MibTable((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1), )
if mibBuilder.loadTexts: panEntityFRUModuleTable.setStatus('current')
panEntityFRUModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: panEntityFRUModuleEntry.setStatus('current')
panEntryFRUModulePowerUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntryFRUModulePowerUsed.setStatus('current')
panEntryFRUModuleNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntryFRUModuleNumPorts.setStatus('current')
panEntityFanTrayTable = MibTable((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1), )
if mibBuilder.loadTexts: panEntityFanTrayTable.setStatus('current')
panEntityFanTrayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: panEntityFanTrayEntry.setStatus('current')
panEntryFanTrayPowerUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntryFanTrayPowerUsed.setStatus('current')
panEntityPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1), )
if mibBuilder.loadTexts: panEntityPowerSupplyTable.setStatus('current')
panEntityPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: panEntityPowerSupplyEntry.setStatus('current')
panEntryPowerSupplyPowerCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEntryPowerSupplyPowerCapacity.setStatus('current')
panEntityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 1))
panEntityMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2))
panEntityMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 1, 1)).setObjects(("PAN-ENTITY-EXT-MIB", "panEntityMIBChassisGroup"), ("PAN-ENTITY-EXT-MIB", "panEntityMIBFRUModuleGroup"), ("PAN-ENTITY-EXT-MIB", "panEntityMIBFanTrayGroup"), ("PAN-ENTITY-EXT-MIB", "panEntityMIBPowerSupplyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panEntityMIBCompliance = panEntityMIBCompliance.setStatus('current')
panEntityMIBChassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 1)).setObjects(("PAN-ENTITY-EXT-MIB", "panEntityTotalPowerAvail"), ("PAN-ENTITY-EXT-MIB", "panEntityTotalPowerUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panEntityMIBChassisGroup = panEntityMIBChassisGroup.setStatus('current')
panEntityMIBFRUModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 2)).setObjects(("PAN-ENTITY-EXT-MIB", "panEntryFRUModulePowerUsed"), ("PAN-ENTITY-EXT-MIB", "panEntryFRUModuleNumPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panEntityMIBFRUModuleGroup = panEntityMIBFRUModuleGroup.setStatus('current')
panEntityMIBFanTrayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 3)).setObjects(("PAN-ENTITY-EXT-MIB", "panEntryFanTrayPowerUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panEntityMIBFanTrayGroup = panEntityMIBFanTrayGroup.setStatus('current')
panEntityMIBPowerSupplyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25461, 1, 1, 7, 2, 2, 4)).setObjects(("PAN-ENTITY-EXT-MIB", "panEntryPowerSupplyPowerCapacity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    panEntityMIBPowerSupplyGroup = panEntityMIBPowerSupplyGroup.setStatus('current')
mibBuilder.exportSymbols("PAN-ENTITY-EXT-MIB", panEntityFRUModuleTable=panEntityFRUModuleTable, panEntryFanTrayPowerUsed=panEntryFanTrayPowerUsed, panEntityMIBCompliance=panEntityMIBCompliance, panEntityTotalPowerUsed=panEntityTotalPowerUsed, panEntityMIBObjects=panEntityMIBObjects, panEntityFanTrayGroup=panEntityFanTrayGroup, panEntityFRUModuleGroup=panEntityFRUModuleGroup, panEntryFRUModulePowerUsed=panEntryFRUModulePowerUsed, panEntityPowerSupplyEntry=panEntityPowerSupplyEntry, panEntryPowerSupplyPowerCapacity=panEntryPowerSupplyPowerCapacity, panEntityPowerSupplyGroup=panEntityPowerSupplyGroup, panEntityMIBModule=panEntityMIBModule, panEntityTotalPowerAvail=panEntityTotalPowerAvail, panEntityFanTrayTable=panEntityFanTrayTable, panEntityMIBPowerSupplyGroup=panEntityMIBPowerSupplyGroup, panEntityPowerSupplyTable=panEntityPowerSupplyTable, panEntityFRUModuleEntry=panEntityFRUModuleEntry, panEntityMIBGroups=panEntityMIBGroups, panEntityMIBChassisGroup=panEntityMIBChassisGroup, panEntityMIBFRUModuleGroup=panEntityMIBFRUModuleGroup, panEntityChassisGroup=panEntityChassisGroup, panEntityMIBFanTrayGroup=panEntityMIBFanTrayGroup, panEntityMIBCompliances=panEntityMIBCompliances, panEntityFanTrayEntry=panEntityFanTrayEntry, panEntryFRUModuleNumPorts=panEntryFRUModuleNumPorts, panEntityMIBConformance=panEntityMIBConformance, PYSNMP_MODULE_ID=panEntityMIBModule)
