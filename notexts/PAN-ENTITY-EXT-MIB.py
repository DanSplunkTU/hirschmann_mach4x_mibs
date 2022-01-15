#
# PySNMP MIB module PAN-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-ENTITY-EXT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:43 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, IpAddress, Integer32, ModuleIdentity, Gauge32, Unsigned32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "IpAddress", "Integer32", "ModuleIdentity", "Gauge32", "Unsigned32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "Counter32")
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
mibBuilder.exportSymbols("PAN-ENTITY-EXT-MIB", panEntityMIBCompliances=panEntityMIBCompliances, panEntityTotalPowerUsed=panEntityTotalPowerUsed, panEntityMIBPowerSupplyGroup=panEntityMIBPowerSupplyGroup, panEntryFRUModulePowerUsed=panEntryFRUModulePowerUsed, panEntityMIBFRUModuleGroup=panEntityMIBFRUModuleGroup, panEntryPowerSupplyPowerCapacity=panEntryPowerSupplyPowerCapacity, panEntityMIBCompliance=panEntityMIBCompliance, panEntityPowerSupplyEntry=panEntityPowerSupplyEntry, panEntityFanTrayGroup=panEntityFanTrayGroup, panEntityMIBModule=panEntityMIBModule, PYSNMP_MODULE_ID=panEntityMIBModule, panEntryFRUModuleNumPorts=panEntryFRUModuleNumPorts, panEntityPowerSupplyTable=panEntityPowerSupplyTable, panEntityFanTrayTable=panEntityFanTrayTable, panEntityMIBFanTrayGroup=panEntityMIBFanTrayGroup, panEntityFanTrayEntry=panEntityFanTrayEntry, panEntityFRUModuleGroup=panEntityFRUModuleGroup, panEntityMIBObjects=panEntityMIBObjects, panEntityPowerSupplyGroup=panEntityPowerSupplyGroup, panEntryFanTrayPowerUsed=panEntryFanTrayPowerUsed, panEntityTotalPowerAvail=panEntityTotalPowerAvail, panEntityFRUModuleEntry=panEntityFRUModuleEntry, panEntityMIBConformance=panEntityMIBConformance, panEntityChassisGroup=panEntityChassisGroup, panEntityFRUModuleTable=panEntityFRUModuleTable, panEntityMIBGroups=panEntityMIBGroups, panEntityMIBChassisGroup=panEntityMIBChassisGroup)
