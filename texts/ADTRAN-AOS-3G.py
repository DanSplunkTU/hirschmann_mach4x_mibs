#
# PySNMP MIB module ADTRAN-AOS-3G (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-3G
# Produced by pysmi-1.1.3 at Sun Nov 21 00:41:07 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSWan = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSWan")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, TimeTicks, Bits, Unsigned32, NotificationType, IpAddress, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Bits", "Unsigned32", "NotificationType", "IpAddress", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
adGenAOS3GMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 6, 2))
adGenAOS3GMib.setRevisions(('2010-01-05 00:00', '2010-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOS3GMib.setRevisionsDescriptions(('Added TEXTUAL-CONVENTION EcioValue and object identifier\n                    adGenAOS3GECIOIntegerValue.\n                    Changes by Reba Holland.', 'Changed syntax of object identifier\n                    adGenAOS3GECIOIntegerValue from EcioValue to Integer32.\n                    Removed TEXTUAL CONVENTION EcioValue.\n                    Changes by Reba Holland.',))
if mibBuilder.loadTexts: adGenAOS3GMib.setLastUpdated('201001050000Z')
if mibBuilder.loadTexts: adGenAOS3GMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOS3GMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                        901 Explorer Blvd.\n                        Huntsville, AL 35806\n\n                        Tel: +1 800 726-8663\n                        Fax: +1 256 963 6217\n                        E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOS3GMib.setDescription('A MIB module for monitoring 3G module values.')
adGenAOS3G = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2))
adGenAOS3GTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0))
if mibBuilder.loadTexts: adGenAOS3GTraps.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GTraps.setDescription('The table contains traps/alarms caused by changes in\n        \t\t\t\tconfiguration values and when statistical data reach\n        \t\t\t\tcertain thresholds.')
adGenAOS3GTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1), )
if mibBuilder.loadTexts: adGenAOS3GTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GTable.setDescription('The table contains 3G cellular statistical data for the cellular\n            interface.')
adGenAOS3GEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GEntry.setDescription('This is an entry into the 3G table.')
adGenAOS3GNetworkAccessID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GNetworkAccessID.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GNetworkAccessID.setDescription('The Network Access ID is the User ID submitted by the 3G\n                Modem during Mobile IP authentication.  For more information,\n                refer to RFC 4282.')
adGenAOS3GHASS = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHASS.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHASS.setDescription('This OID displays whether the shared secret for the home\n                agent has been set for Mobile IP authentication.')
adGenAOS3GHASPI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHASPI.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHASPI.setDescription('The Home Agent Security Parameter Index uniquely identifies a\n                security association for the home agent for use during Mobile\n                IP authentication.')
adGenAOS3GAAASS = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 4), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GAAASS.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GAAASS.setDescription('This OID displays whether the shared secret for AAA\n                has been set for Mobile IP authentication.')
adGenAOS3GAAASPI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GAAASPI.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GAAASPI.setDescription('The AAA Security Parameter Index uniquely identifies a\n                security association for AAA for use during Mobile IP\n                authentication.')
adGenAOS3GReverseTunneling = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 6), Bits().clone(namedValues=NamedValues(("unset", 0), ("set", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GReverseTunneling.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GReverseTunneling.setDescription("This OID describes if a tunnel is setup from the\n                3G module's care of address to the home agent.  A care of\n                address is a temporary IP address for a mobile device.")
adGenAOS3GHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHomeAddress.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHomeAddress.setDescription('The permanent home IP address for the 3G\n                 module in the cellular network.')
adGenAOS3GPrimaryHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPrimaryHomeAddress.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GPrimaryHomeAddress.setDescription("The primary IP address of the 3G module's home agent.")
adGenAOS3GSecHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GSecHomeAddress.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GSecHomeAddress.setDescription("The secondary IP address of the 3G module's home agent.")
adGenAOS3GRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GRSSI.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GRSSI.setDescription('The Receive Signal Strength Indicator for the cellular\n                connection. This value is a measurement of signal strength.')
adGenAOS3GECIO = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GECIO.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GECIO.setDescription('The Ec/Io for the cellular connection.  This is the ratio of\n                received pilot energy to the total received energy.  The value\n                is similar to signal-to-noise ratio.')
adGenAOS3GPnOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPnOffset.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GPnOffset.setDescription('The Pn Offset for the cellular connection.  Base stations\n                assigned to a particular frequency carrier operate at the same\n                center frequency.  The PN offset is used to distinguish base\n                stations from one another.')
adGenAOS3GServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GServiceType.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GServiceType.setDescription('The current Cellular Service Type for\n                the cellular connection.')
adGenAOS3GServiceTypePreference = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 9, 10))).clone(namedValues=NamedValues(("modeAUTO", 4), ("mode1xRTT", 9), ("mode1xEVDO", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GServiceTypePreference.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GServiceTypePreference.setDescription('The current Cellular Service Type Preference for the cellular\n                connection.  Cellular Service Type can be forced to 1xRTT mode\n                or 1xEVDO mode.  By default, it is set to Hybrid or AUTO mode\n                 which chooses the best available signal.')
adGenAOS3GConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GConnectionState.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GConnectionState.setDescription('The current Connection State for the cellular connection.')
adGenAOS3GECIOIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GECIOIntegerValue.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GECIOIntegerValue.setDescription('The Ec/Io for the cellular connection displayed in integer\n                form. This is the ratio of received pilot energy to the total\n                received energy. The value is similar to signal-to-noise ratio.\n                EC/IO values typically are represented as a value with a\n                decimal place. In this representation the value will be\n                scaled by 10.  Hence a value of 1.5 will be represented as 15.')
adGenAOS3GHardwareDataTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2), )
if mibBuilder.loadTexts: adGenAOS3GHardwareDataTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHardwareDataTable.setDescription('The table contains profile information\n            for the 3G cellular interface.')
adGenAOS3GHardwareDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GHardwareDataEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHardwareDataEntry.setDescription('This is an entry into the 3G hardware data table.')
adGenAOS3GSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GSystemID.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GSystemID.setDescription('The System Identification number is the identifier\n                for a cellular network in a certain area.')
adGenAOS3GNetworkID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GNetworkID.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GNetworkID.setDescription('The Network Identification number identifies a subset\n                of a particular SID corresponding to different networks.')
adGenAOS3GPrefferedRoamList = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GPrefferedRoamList.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GPrefferedRoamList.setDescription('The PRL is a database of cell towers that the cellular modem\n                can roam on.  This OID specifies the current version of\n                that database that is programmed onto the cellular modem.')
adGenAOS3GMobileDirNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GMobileDirNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GMobileDirNumber.setDescription('The MDN is the 10 digit phone number assigned to\n                the 3G module.')
adGenAOS3GESN = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GESN.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GESN.setDescription('The Electronic Serial Number is is a unique\n                number that identifies the 3G module.')
adGenAOS3GMobileStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GMobileStationID.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GMobileStationID.setDescription('The MSID is a 10 digit number that identifies\n                the 3G module in the network.')
adGenAOS3GHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GHardwareVersion.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHardwareVersion.setDescription('The hardware version of the 3G modem.')
adGenAOS3GFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS3GFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GFirmwareVersion.setDescription('The firmware version of the 3G modem.')
adGenAOS3GThresholdDataTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3), )
if mibBuilder.loadTexts: adGenAOS3GThresholdDataTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GThresholdDataTable.setDescription('The table contains settings regarding whether the trap is enabled\n            and threshold values for certain traps.')
adGenAOS3GThresholdDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOS3GThresholdDataEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GThresholdDataEntry.setDescription('This is an entry into the 3G threshold data table.')
adGenAOS3GEnableTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GEnableTraps.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GEnableTraps.setDescription('This OID indicates whether traps\n                are enabled for the interface.')
adGenAOS3GRSSIThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GRSSIThreshold.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GRSSIThreshold.setDescription('This is a value from (-200..200) that sets the threshold for\n                an RSSI trap to occur.  When the RSSI is below this value, it\n                will cause an RSSI alarm trap.  When the RSSI rises above this\n                value, it will cause an RSSI cleared trap.')
adGenAOS3GECIOThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOS3GECIOThreshold.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GECIOThreshold.setDescription('This is a value from (-200..200) that sets the threshold for\n                an ECIO trap to occur.  When the ECIO is below this value, it\n                will cause an ECIO alarm trap.  When the ECIO rises above this\n                value, it will cause an ECIO cleared trap.')
rssiDataRangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
if mibBuilder.loadTexts: rssiDataRangeAlarm.setStatus('current')
if mibBuilder.loadTexts: rssiDataRangeAlarm.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that the RSSI data value object for\n            the 3G cellular interface has exceeded the range specified by the\n            user.')
ecioDataRangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
if mibBuilder.loadTexts: ecioDataRangeAlarm.setStatus('current')
if mibBuilder.loadTexts: ecioDataRangeAlarm.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that the ECIO data value object for\n            the 3G cellular interface has exceeded the range specified by the\n            user.')
rssiDataRangeClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
if mibBuilder.loadTexts: rssiDataRangeClear.setStatus('current')
if mibBuilder.loadTexts: rssiDataRangeClear.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that the RSSI data value object for\n            the 3G cellular interface has returned to the range specified by\n            the user.')
ecioDataRangeClear = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
if mibBuilder.loadTexts: ecioDataRangeClear.setStatus('current')
if mibBuilder.loadTexts: ecioDataRangeClear.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that the ECIO data value object for\n            the 3G cellular interface has returned to the range specified by\n            the user.')
configValueSet = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: configValueSet.setStatus('current')
if mibBuilder.loadTexts: configValueSet.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that a data value object for the 3G\n            cellular interface from the 3G Hardware Table has been modified\n            from the previous state.')
modemResetAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: modemResetAlarm.setStatus('current')
if mibBuilder.loadTexts: modemResetAlarm.setDescription('This trap signifies that the SNMP entity, acting in\n            an agent role, has detected that the 3G modem has been reset.')
serviceTypeChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 7)).setObjects(("IF-MIB", "ifIndex"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"))
if mibBuilder.loadTexts: serviceTypeChangeAlarm.setStatus('current')
if mibBuilder.loadTexts: serviceTypeChangeAlarm.setDescription('This trap signifies that the SNMP entity, acting\n            in an agent role, has detected that the service type for the 3G\n            cellular interface has changed.')
connectionStateDownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: connectionStateDownAlarm.setStatus('current')
if mibBuilder.loadTexts: connectionStateDownAlarm.setDescription('This trap signifies that the SNMP entity, acting\n            in an agent role, has detected that the connection status of the\n            modem has gone down from either DORMANT or a CONNECTED state.')
adGenAOS3GConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9))
adGenAOS3GGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1))
adGenAOS3GCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2))
adGenAOS3GFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2, 1)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GTableGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GHardwareDataGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GThresholdDataGroup"), ("ADTRAN-AOS-3G", "adGenAOS3GTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GFullCompliance = adGenAOS3GFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n            version 2 of the adGenAOS3G MIB.')
adGenAOS3GTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 1)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GNetworkAccessID"), ("ADTRAN-AOS-3G", "adGenAOS3GHASS"), ("ADTRAN-AOS-3G", "adGenAOS3GHASPI"), ("ADTRAN-AOS-3G", "adGenAOS3GAAASS"), ("ADTRAN-AOS-3G", "adGenAOS3GAAASPI"), ("ADTRAN-AOS-3G", "adGenAOS3GReverseTunneling"), ("ADTRAN-AOS-3G", "adGenAOS3GHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GPrimaryHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GSecHomeAddress"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"), ("ADTRAN-AOS-3G", "adGenAOS3GECIO"), ("ADTRAN-AOS-3G", "adGenAOS3GPnOffset"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"), ("ADTRAN-AOS-3G", "adGenAOS3GServiceTypePreference"), ("ADTRAN-AOS-3G", "adGenAOS3GConnectionState"), ("ADTRAN-AOS-3G", "adGenAOS3GECIOIntegerValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GTableGroup = adGenAOS3GTableGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GTableGroup.setDescription('This group contains 3G cellular statistical data for profile\n            information.')
adGenAOS3GHardwareDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 2)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GSystemID"), ("ADTRAN-AOS-3G", "adGenAOS3GNetworkID"), ("ADTRAN-AOS-3G", "adGenAOS3GPrefferedRoamList"), ("ADTRAN-AOS-3G", "adGenAOS3GMobileDirNumber"), ("ADTRAN-AOS-3G", "adGenAOS3GESN"), ("ADTRAN-AOS-3G", "adGenAOS3GMobileStationID"), ("ADTRAN-AOS-3G", "adGenAOS3GHardwareVersion"), ("ADTRAN-AOS-3G", "adGenAOS3GFirmwareVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GHardwareDataGroup = adGenAOS3GHardwareDataGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GHardwareDataGroup.setDescription('This group contains 3G cellular statistical data for hardware\n            information.')
adGenAOS3GThresholdDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 3)).setObjects(("ADTRAN-AOS-3G", "adGenAOS3GEnableTraps"), ("ADTRAN-AOS-3G", "adGenAOS3GRSSIThreshold"), ("ADTRAN-AOS-3G", "adGenAOS3GECIOThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GThresholdDataGroup = adGenAOS3GThresholdDataGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GThresholdDataGroup.setDescription('This group contains threshold data for enabling 3G interface\n            thresholds.')
adGenAOS3GTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 4)).setObjects(("ADTRAN-AOS-3G", "rssiDataRangeAlarm"), ("ADTRAN-AOS-3G", "ecioDataRangeAlarm"), ("ADTRAN-AOS-3G", "rssiDataRangeClear"), ("ADTRAN-AOS-3G", "ecioDataRangeClear"), ("ADTRAN-AOS-3G", "configValueSet"), ("ADTRAN-AOS-3G", "modemResetAlarm"), ("ADTRAN-AOS-3G", "serviceTypeChangeAlarm"), ("ADTRAN-AOS-3G", "connectionStateDownAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOS3GTrapGroup = adGenAOS3GTrapGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOS3GTrapGroup.setDescription('Traps which may be used to enhance event driven\n            management of the interface.')
mibBuilder.exportSymbols("ADTRAN-AOS-3G", adGenAOS3GTrapGroup=adGenAOS3GTrapGroup, adGenAOS3GHomeAddress=adGenAOS3GHomeAddress, connectionStateDownAlarm=connectionStateDownAlarm, adGenAOS3GGroup=adGenAOS3GGroup, adGenAOS3GESN=adGenAOS3GESN, adGenAOS3GFullCompliance=adGenAOS3GFullCompliance, adGenAOS3GRSSIThreshold=adGenAOS3GRSSIThreshold, adGenAOS3GHardwareDataGroup=adGenAOS3GHardwareDataGroup, adGenAOS3GPrefferedRoamList=adGenAOS3GPrefferedRoamList, adGenAOS3GECIO=adGenAOS3GECIO, adGenAOS3GHardwareDataTable=adGenAOS3GHardwareDataTable, adGenAOS3GCompliances=adGenAOS3GCompliances, adGenAOS3GHASPI=adGenAOS3GHASPI, adGenAOS3GRSSI=adGenAOS3GRSSI, adGenAOS3GThresholdDataGroup=adGenAOS3GThresholdDataGroup, rssiDataRangeAlarm=rssiDataRangeAlarm, adGenAOS3GThresholdDataEntry=adGenAOS3GThresholdDataEntry, adGenAOS3GThresholdDataTable=adGenAOS3GThresholdDataTable, adGenAOS3GTable=adGenAOS3GTable, adGenAOS3GECIOThreshold=adGenAOS3GECIOThreshold, adGenAOS3GNetworkID=adGenAOS3GNetworkID, adGenAOS3GSystemID=adGenAOS3GSystemID, adGenAOS3GTraps=adGenAOS3GTraps, rssiDataRangeClear=rssiDataRangeClear, adGenAOS3GHASS=adGenAOS3GHASS, adGenAOS3GServiceTypePreference=adGenAOS3GServiceTypePreference, adGenAOS3GMobileDirNumber=adGenAOS3GMobileDirNumber, adGenAOS3GConformance=adGenAOS3GConformance, adGenAOS3GConnectionState=adGenAOS3GConnectionState, adGenAOS3GReverseTunneling=adGenAOS3GReverseTunneling, modemResetAlarm=modemResetAlarm, serviceTypeChangeAlarm=serviceTypeChangeAlarm, adGenAOS3GPnOffset=adGenAOS3GPnOffset, adGenAOS3GMobileStationID=adGenAOS3GMobileStationID, adGenAOS3GTableGroup=adGenAOS3GTableGroup, adGenAOS3GEnableTraps=adGenAOS3GEnableTraps, ecioDataRangeClear=ecioDataRangeClear, adGenAOS3GMib=adGenAOS3GMib, adGenAOS3GSecHomeAddress=adGenAOS3GSecHomeAddress, adGenAOS3GAAASS=adGenAOS3GAAASS, adGenAOS3GHardwareVersion=adGenAOS3GHardwareVersion, adGenAOS3GPrimaryHomeAddress=adGenAOS3GPrimaryHomeAddress, ecioDataRangeAlarm=ecioDataRangeAlarm, adGenAOS3GEntry=adGenAOS3GEntry, adGenAOS3GECIOIntegerValue=adGenAOS3GECIOIntegerValue, adGenAOS3GAAASPI=adGenAOS3GAAASPI, adGenAOS3GNetworkAccessID=adGenAOS3GNetworkAccessID, adGenAOS3GServiceType=adGenAOS3GServiceType, adGenAOS3GHardwareDataEntry=adGenAOS3GHardwareDataEntry, PYSNMP_MODULE_ID=adGenAOS3GMib, adGenAOS3GFirmwareVersion=adGenAOS3GFirmwareVersion, configValueSet=configValueSet, adGenAOS3G=adGenAOS3G)
