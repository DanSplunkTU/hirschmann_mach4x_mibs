#
# PySNMP MIB module SYMM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/microsemi/SYMM-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 18:12:41 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("RFC-1212", "ObjectIdentity", "ModuleIdentity")
Unsigned32, Integer32 = mibBuilder.importSymbols("RFC1155-SMI", "Unsigned32", "Integer32")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, iso, enterprises, ModuleIdentity, IpAddress, MibIdentifier, ObjectIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Unsigned32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "iso", "enterprises", "ModuleIdentity", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmetricom = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070))
symmetricom.setRevisions(('2009-06-11 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmetricom.setRevisionsDescriptions(('rbb - Cleaning up errors in the mib metadata',))
if mibBuilder.loadTexts: symmetricom.setLastUpdated('200906111200Z')
if mibBuilder.loadTexts: symmetricom.setOrganization('Symmetricom, Inc.')
if mibBuilder.loadTexts: symmetricom.setContactInfo('\n            Symmetricom, Inc.\n            2300 Orchard Parkway\n            San Jose, CA 95131')
if mibBuilder.loadTexts: symmetricom.setDescription("This is the MIB Module for Symmetricom's enterprise specific\n        parameters.")
symmNetworkManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1))
if mibBuilder.loadTexts: symmNetworkManagement.setStatus('current')
if mibBuilder.loadTexts: symmNetworkManagement.setDescription('This is the root object identifier for all MIBS under the\n        Symmetricom tree.')
symmCmipManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 1))
if mibBuilder.loadTexts: symmCmipManagement.setStatus('current')
if mibBuilder.loadTexts: symmCmipManagement.setDescription('This is the root object identifier for CMIP based objects.')
symmSnmpManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2))
if mibBuilder.loadTexts: symmSnmpManagement.setStatus('current')
if mibBuilder.loadTexts: symmSnmpManagement.setDescription('This is the root object identifier for SNMP based objects.')
symmTimePictra = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 1))
if mibBuilder.loadTexts: symmTimePictra.setStatus('current')
if mibBuilder.loadTexts: symmTimePictra.setDescription("This is reserved for objects related to Symmetricom's TimePictra\n        products.")
symmBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 2))
if mibBuilder.loadTexts: symmBroadband.setStatus('current')
if mibBuilder.loadTexts: symmBroadband.setDescription("The subtree that contains objects related to Symmetricom's GoWide\n        products.")
symmTTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3))
if mibBuilder.loadTexts: symmTTM.setStatus('current')
if mibBuilder.loadTexts: symmTTM.setDescription("The subtree that contains objects related to Symmetricom's\n        Timing, Test and Measurement products.")
products = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1))
experiment = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 99))
ts2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 1))
nts = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 2))
ts2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 3))
s100 = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 4))
syncserver = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5))
xli = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 6))
version = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1))
ntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1))
tyming = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2))
gps = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3))
dialup = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 4))
net = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 5))
etc = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6))
ntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysLeap.setStatus('current')
if mibBuilder.loadTexts: ntpSysLeap.setDescription('NTP Leap Indicator.  This is a two-bit code \n        warning of an impending leap second to be inserted\n        into the NTP timescale.  The bits are set before\n        23:59 on the day of insertion and reset after 00:00\n        on the following day.  This causes the number of\n        seconds (rollover interval) in the day of insertion\n        to be increased or decreased by one.  In the case\n        of primary servers the bits are set by operator \n        intervention, while in the case of secondary servers\n        the bits are set by the protocol.  The two bits, \n        bit 0 and bit 1, respectively, are coded as follows:\n        ===================================================\n        00      no warning\n        01      last minute has 61 seconds\n        10      last minute has 59 seconds\n        11      alarm condition(clock not synchronized)\n        ===================================================\n        In all except the alarm condition(11), NTP itself\n        does nothing with these bits, except pass them on to\n        the time-conversion routines that are not part of\n        NTP.  The alarm condition occurs when, for whatever\n        reason, the local clock is not synchronized, such \n        as when first coming up or after an extended period\n        when no primary reference source is available.')
ntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysStratum.setStatus('current')
if mibBuilder.loadTexts: ntpSysStratum.setDescription('Current NTP stratum level.  This is an integer\n        indicating the stratum of the local clock with\n        values defined as follows:\n        ================================================\n        0       unspecified\n        1       primary reference (e.g., calibrated atomic\n                    clock, radio clock)\n        2-255   secondary reference (via NTP)\n        ================================================')
ntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPrecision.setStatus('current')
if mibBuilder.loadTexts: ntpSysPrecision.setDescription('Current NTP precision value.  This is a signed\n        integer indicating the precision of the various\n        clocks, in seconds to the nearest power of two.\n        The value must be rounded to the next larger power\n        of two; for instance, a 50-Hz (20ms) or 60-Hz (16.17ms)\n        power-frequency clock would be assigned the value \n        -5 (31.25ms), while a 1000-Hz (1ms) crystal-controlled\n        clock would be assigned the value -9 (1.95ms).')
ntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRootDelay.setStatus('current')
if mibBuilder.loadTexts: ntpSysRootDelay.setDescription('Total roundtrip delay to the primary reference \n        source at the root of the synchronization\n        subnet, in seconds. Also known as root distance.')
ntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRootDispersion.setStatus('current')
if mibBuilder.loadTexts: ntpSysRootDispersion.setDescription('Maximum error relative to the primary reference \n        source at the root of the synchronization subnet, \n        in seconds.  Only positive values greater than \n        zero are possible.')
ntpSysRefID = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRefID.setStatus('current')
if mibBuilder.loadTexts: ntpSysRefID.setDescription('NTP Reference Clock Identifier.  This is a\n        32 bit code identifying the particular reference\n        clock.  In the case of stratum 0 (unspecified) or\n        stratum 1 (primary reference), this is a four-\n        octet, left-justified, zero-padded ASCII string.\n        While not enumerated as part of the NTP spec, the\n        following are suggested ASCII identifiers:\n        ==============================================\n        DCN             DCN routing protocol\n        NIST            NIST public modem\n        TSP             TSP time protocol\n        DTS             Digital Time Service\n        ATOM            Atomic clock (calibrated)\n        VLF             VLF radio (OMEGA,etc.)\n        callsign        Generic radio\n        LORC            LORAN-C radionavigation\n        GOES            GOES UHF environment satellite\n        GPS             GPS UHF satellite positioning\n        ==============================================\n        \n        The following ref ids are used by the SyncServer:\n        ==============================================\n        GPS             GPS satellite)\n        IRIG            IRIG B timecode\n        PPS             Ext. 1 PPS input\n        E10M\t        Ext. 10 MHz input\n        FREE            Internal Clock\n        FLY             Internal Clock after the Hardware\n                        Clock reference is lost\n        ==============================================')
ntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysRefTime.setStatus('current')
if mibBuilder.loadTexts: ntpSysRefTime.setDescription('NTP Reference Timestamp.  This is the time,\n        in timestamp format (converted to DisplayString), \n        when the local clock was last updated.  If the\n        local clock has never been synchronized, the value\n        is zero.')
ntpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPoll.setStatus('current')
if mibBuilder.loadTexts: ntpSysPoll.setDescription('Minimum interval between transmitted messages, in \n        seconds as a power of two.  For instance, a value \n        of six indicates a minimum interval of 64 seconds.')
ntpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPeer.setStatus('current')
if mibBuilder.loadTexts: ntpSysPeer.setDescription('Current synchronization source.  In stratum > 1 this\n        variable returns the decimal representation of the \n        IPv4 address of its current peer. In stratum = 1 this \n        variable returns the decimal representation of the\n        hardware clock which is 2981759.')
ntpSysPhase = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPhase.setStatus('current')
if mibBuilder.loadTexts: ntpSysPhase.setDescription('System clock offset from the selected source.')
ntpSysFreq = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysFreq.setStatus('current')
if mibBuilder.loadTexts: ntpSysFreq.setDescription('System clock frequency correction from ntpd.')
ntpSysError = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysError.setStatus('current')
if mibBuilder.loadTexts: ntpSysError.setDescription('Current system error from ntpd.')
ntpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysClock.setStatus('current')
if mibBuilder.loadTexts: ntpSysClock.setDescription('Current system time from ntpd. This is usually \n        derived from the hardware clock but could be \n        from any other ntp source.')
ntpSysSystem = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysSystem.setStatus('current')
if mibBuilder.loadTexts: ntpSysSystem.setDescription('Description of the current system.')
ntpSysProcessor = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysProcessor.setStatus('current')
if mibBuilder.loadTexts: ntpSysProcessor.setDescription('Type of local processor.')
ntpSysNotrust = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysNotrust.setStatus('mandatory')
if mibBuilder.loadTexts: ntpSysNotrust.setDescription('Force authentication.')
ntpSysPktsReceived = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32768))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysPktsReceived.setStatus('mandatory')
if mibBuilder.loadTexts: ntpSysPktsReceived.setDescription('This variable is a rollover counter which reflects \n        the number of ntp packets received by the SyncServer.\n        It is valid for all versions of the SyncServer.')
ntpSysMode = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symactive", 1), ("sympassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedctl", 6), ("reservedpriv", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysMode.setStatus('mandatory')
if mibBuilder.loadTexts: ntpSysMode.setDescription('An integer indicating the NTP association mode  \n        and are coded as follows:\n        ============================================\n        0       unspecified\n        1       symmetric active\n        2       symmetric passive\n        3       client\n        4       server\n        5       broadcast\n        6       reserved for NTP control messages\n        7       reserved for private use\n        ============================================')
ntpSysVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntpSysVersion.setStatus('current')
if mibBuilder.loadTexts: ntpSysVersion.setDescription('The version of the NTP daemon on the system.')
tymingStatus = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingStatus.setStatus('current')
if mibBuilder.loadTexts: tymingStatus.setDescription('Indicates what status the Hardware Clock considers \n        itself to be as a timing source defined as follows:\n        ============================================\n        Good     HW Clock has a valid time reference.\n        Bad      HW Clock has no valid time reference.\n        ============================================')
tymingSource = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingSource.setStatus('current')
if mibBuilder.loadTexts: tymingSource.setDescription('The time or frequency source currently in use \n        by the Hardware Clock defined as follows:\n        ============================================\n         0       None\n             1       GPS\n             8       IRIG\n        16       External 1PPS\n        24       External 10 MHz\n        31       Freerun\n        ============================================')
tymingTime = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingTime.setStatus('current')
if mibBuilder.loadTexts: tymingTime.setDescription('The time according to the Hardware Clock in \n        the format of:\n\n        WWW MMM dd hh:mm:ss yyyy\n\n        defined as follows:\n            ============================================\n            WWW              weekday\n            MMM              character month\n            dd               day of month\n            hh:mm:ss         time\n            yyyy             year\n\n        Example          Thu Sep 21 23:46:09 2006\n        ============================================')
tymingVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingVersion.setStatus('current')
if mibBuilder.loadTexts: tymingVersion.setDescription("The version of the software on the SyncServer's \n        Hardware Clock.")
tymingFlyPeriod = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tymingFlyPeriod.setStatus('current')
if mibBuilder.loadTexts: tymingFlyPeriod.setDescription('This variable is not currently used and returns zero.')
gpsPosition = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsPosition.setStatus('current')
if mibBuilder.loadTexts: gpsPosition.setDescription('Returns the current position in the format of:\n\n        A BB CC DD EEE F GGG HH II JJJ KK\n        \n        defined as follows:\n            ===============================================\n        A           sign of the latitude \n                    (1 = North, -1 = South)\n        BB          degrees of the latitude  \n        CC          minutes of the latitude\n        DD          seconds of the latitude\n        EEE         milliseconds of the latitude\n        F           sign of the longitude \n                    (1 = East, -1 = West)\n        GGG         degrees of the longitude\n        HH          minutes of the longitude\n        II          seconds of the longitude\n        JJJ         milliseconds of the longitude\n        KK          altitude in meters\n        ===============================================')
gpsUTCOffset = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsUTCOffset.setStatus('current')
if mibBuilder.loadTexts: gpsUTCOffset.setDescription('This variable is reserved for future use.')
gpsHealth = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsHealth.setStatus('current')
if mibBuilder.loadTexts: gpsHealth.setDescription("This is the GPS receiver health status defined as\n        follows:\n        ======================================================\n        0 = Receiver Down       The Hardware Clock can't \n                                communicate with the receiver.\n\n        1 = Unknown Mode        An undefined mode of the GPS\n                                receiver.\n\n        2 = Acquiring Signal    The receiver is attempting to\n                                track a GPS signal.\n\n        3 = Bad Geometry        The geometry of the tracked\n                                satellites is unsatisfactory for\n                                a position solution.\n\n        4 = Propagate Mode      A position estimation mode used\n                                in highly dynamic environments.\n\n        5 = 2d Solution         The receiver is able to perform \n                                position fixes for latitude and \n                                longitude but does not have \n                                enough satellites for altitude.\n\n        6 = 3d Solution         The receiver is now able to \n                                perform position fixes for \n                                latitude, longitude and altitude.\n\n        7 = Position Hold       Position fixes are no longer \n                                attempted, and the user entered \n                                or surveyed position is used.\n\n        8 = Time Valid          The receiver has valid timing \n                                information from GPS satellites \n                                (including current leap second \n                                information).  This is the final \n                                state for all configured GPS modes.\n        ======================================================")
gpsSatlist = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsSatlist.setStatus('current')
if mibBuilder.loadTexts: gpsSatlist.setDescription('Displays the GPS satellite tracking information in the\n        format of:\n\n        N,X1,Y1,Z1,...,XN,YN,ZN\n\n        defined as follows:\n        ======================================================\t\n        N        Number of satellites. If one or more satellites \n                 are available, Xi,Yi,Zi follows N.\n\n        Xi       Satellite vehicle number.\n\n        Yi       Satellite signal strength in dBW where less \n                 than -200 dBW means no signal.\n\n        Zi       Zi can be either T or C. T(racking) means the \n                 SyncServer receives the information from the \n                 satellite but the information is not used in its \n                 timing solution. C(urrent) means the SyncServer \n                 currently uses satellite information in its \n                 timing solution.\n        \n        Examples\n\n        For no satellites:\n        0\n\n        For one satellite with vehicle number 16:\n        1,16,C,-158\n\n        For six satellites:\n        6,12,C,-156,14,C,-155,8,T,-162,24,C,-158,18,C,161,6,C,-160\t\n        ======================================================')
gpsMode = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpsMode.setStatus('current')
if mibBuilder.loadTexts: gpsMode.setDescription("The mode of the GPS receiver defined as follows:\n        ======================================================\n        Receiver Mode: Survey. \n\n        The receiver is surveying and averaging its position. \n        When it has finished surveying, the receiver switches \n        to Position Hold mode. Survey mode and Position Hold \n        mode are appropriate for static applications, such as a \n        typical server room environment. This is the default mode \n        when the SyncServer starts.\n\n        Receiver Mode: Dynamic. \n\n        The GPS receiver surveys continuously to determine its \n        position and doesn't switch to another mode. This mode \n        must be initiated by a user, and is appropriate for mobile \n        applications such as ships, land vehicles, and aircraft. \n        The degree of accuracy this mode offers is fine for NTP \n        time over networks, but is less than optimal for the IRIG-B, \n        1 PPS, 10 MHz outputs available on some SyncServer models.  \n\n        Receiver Mode: Hold. \n\n        The GPS receiver has completed Survey mode and switched to \n        this mode, or the user has manually entered a position and \n        forced it into this mode. The accuracy and stability of the \n        SyncServer's timing outputs are optimal when the receiver \n        has its exact position and is in this mode.\n        ======================================================")
etcVersion = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcVersion.setStatus('current')
if mibBuilder.loadTexts: etcVersion.setDescription('Version info for SyncServer system.')
etcSerialNbr = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcSerialNbr.setStatus('current')
if mibBuilder.loadTexts: etcSerialNbr.setDescription('Unique serial number factory programmed into each unit.')
etcModel = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcModel.setStatus('current')
if mibBuilder.loadTexts: etcModel.setDescription('Model type factory programmed into each unit.')
etcUpgrade = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcUpgrade.setStatus('current')
if mibBuilder.loadTexts: etcUpgrade.setDescription('Describes whether or not an upgrade is available from\n        the upgrade server described as follows:\n        ======================================================\n        0       No upgrade is available.\n        1       An upgrade is available.\n        ======================================================')
etcUpgradeServer = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcUpgradeServer.setStatus('current')
if mibBuilder.loadTexts: etcUpgradeServer.setDescription('Address of the server where new upgrades can be\n        downloaded.')
etcAlarmString = MibScalar((1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etcAlarmString.setStatus('current')
if mibBuilder.loadTexts: etcAlarmString.setDescription('Defines the format for the system alarm traps.  This is \n        only valid embedded in a trap message.')
etcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9070) + (0,0)).setObjects(("SYMM-SMI", "etcAlarmString"))
if mibBuilder.loadTexts: etcAlarm.setDescription('The trap provides notification of Hardware Clock, NTP,\n        system, and network alarms events.  The user can configure\n        which alarms send traps on the ADMIN - Alarms page.')
mibBuilder.exportSymbols("SYMM-SMI", ntpSysRootDelay=ntpSysRootDelay, tymingVersion=tymingVersion, ntpSysRefID=ntpSysRefID, symmetricom=symmetricom, ntpSysRootDispersion=ntpSysRootDispersion, symmTimePictra=symmTimePictra, gpsHealth=gpsHealth, tymingStatus=tymingStatus, PYSNMP_MODULE_ID=symmetricom, ntpSysNotrust=ntpSysNotrust, symmTTM=symmTTM, ntpSysClock=ntpSysClock, gpsUTCOffset=gpsUTCOffset, etcVersion=etcVersion, ntpSysFreq=ntpSysFreq, xli=xli, ntpSysPoll=ntpSysPoll, symmCmipManagement=symmCmipManagement, ntpSysLeap=ntpSysLeap, ntpSysRefTime=ntpSysRefTime, products=products, tymingSource=tymingSource, etcSerialNbr=etcSerialNbr, ntpSysStratum=ntpSysStratum, tyming=tyming, etcAlarmString=etcAlarmString, gpsSatlist=gpsSatlist, dialup=dialup, etcUpgrade=etcUpgrade, symmSnmpManagement=symmSnmpManagement, etcUpgradeServer=etcUpgradeServer, ntpSystem=ntpSystem, ntpSysVersion=ntpSysVersion, experiment=experiment, net=net, etcAlarm=etcAlarm, tymingFlyPeriod=tymingFlyPeriod, gpsPosition=gpsPosition, ntpSysProcessor=ntpSysProcessor, tymingTime=tymingTime, ntpSysPktsReceived=ntpSysPktsReceived, gpsMode=gpsMode, ts2000=ts2000, ntpSysPeer=ntpSysPeer, ntpSysPhase=ntpSysPhase, ntpSysSystem=ntpSysSystem, gps=gps, ntpSysError=ntpSysError, s100=s100, symmBroadband=symmBroadband, ntpSysMode=ntpSysMode, version=version, ntpSysPrecision=ntpSysPrecision, syncserver=syncserver, etc=etc, symmNetworkManagement=symmNetworkManagement, etcModel=etcModel, ts2100=ts2100, nts=nts)
