# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu


# Steer torque limits

class CarControllerParams:
  STEER_MAX = 800                # theoretical max_steer 2047
  STEER_DELTA_UP = 10             # torque increase per refresh
  STEER_DELTA_DOWN = 25           # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 15     # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 1     # weight driver torque
  STEER_DRIVER_FACTOR = 1         # from dbc
  STEER_ERROR_MAX = 350           # max delta between torque cmd and torque motor

class CAR:
  CX5 = "Mazda CX-5 2017"
  CX9 = "Mazda CX-9 2017"
  Mazda3 = "Mazda3 2017"

class LKAS_LIMITS:
  STEER_THRESHOLD = 15
  DISABLE_SPEED = 45    # kph
  ENABLE_SPEED = 52     # kph

class Buttons:
  NONE = 0
  SET_PLUS = 1
  SET_MINUS = 2
  RESUME = 3
  CANCEL = 4

FINGERPRINTS = {
  CAR.CX5: [
    # CX-5 2017 GT
    {
      64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 605: 8, 606: 8, 607: 8, 608: 8, 628: 8, 832: 8, 836: 8, 863: 8, 865: 8, 866: 8, 867: 8, 868: 8, 869: 8, 870: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1070: 8, 1078: 8, 1080: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1139: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1177: 8, 1178: 8, 1179: 8, 1180: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1243: 8, 1244: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1270: 8, 1271: 8, 1272: 8, 1274: 8, 1275: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1446: 8, 1456: 8, 1479: 8
    },

    # CX-5 2019 GTR
    {
      64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 254: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 605: 8, 606: 8, 607: 8, 608: 8, 628: 8, 736: 8, 832: 8, 836: 8, 863: 8, 865: 8, 866: 8, 867: 8, 868: 8, 869: 8, 870: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1078: 8, 1080: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1139: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1170: 8, 1171: 8, 1173: 8, 1177: 8, 1178: 8, 1179: 8, 1180: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1244: 8, 1260: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1270: 8, 1271: 8, 1272: 8, 1274: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1446: 8, 1456: 8, 1479: 8, 1776: 8, 1792: 8, 1872: 8, 1937: 8, 1953: 8, 1968: 8, 2015: 8, 2016: 8, 2024: 8
    }
  ],

  CAR.CX9: [
    # CX-9 2017 Australia - old CAM connector
    {
      64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 138: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 522: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 583: 8, 605: 8, 606: 8, 628: 8, 832: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1078: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1139: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1170: 8, 1177: 8, 1180: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1243: 8, 1244: 8, 1247: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1271: 8, 1272: 8, 1274: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1446: 8, 1456: 8, 1479: 8
    },

    # CX-9 2016 - old CAM connector
    {
      64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 583: 8, 605: 8, 606: 8, 608: 8, 628: 8, 832: 8, 836: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1078: 8, 1080: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1139: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1170: 8, 1177: 8, 1178: 8, 1179: 8, 1180: 8, 1181: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1244: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1271: 8, 1272: 8, 1274: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1446: 8, 1456: 8, 1479: 8, 1792: 8, 1872: 8, 1937: 8, 1953: 8, 1968: 8, 1988: 8, 1996: 8, 2000: 8, 2001: 8, 2004: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
    }
  ],

  CAR.Mazda3: [
    # Mazda 3 2017
    {
      19: 5, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 605: 8, 606: 8, 607: 8, 628: 8, 832: 8, 863: 8, 865: 8, 866: 8, 867: 8, 868: 8, 869: 8, 870: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1070: 8, 1078: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1169: 8, 1170: 8, 1173: 8, 1177: 8, 1180: 8, 1182: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1243: 8, 1244: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1270: 8, 1271: 8, 1272: 8, 1274: 8, 1275: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1456: 8, 1479: 8, 2015: 8, 2024: 8, 2025: 8
    },

    # Mazda 6 2017 GT
    {
      64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 605: 8, 606: 8, 607: 8, 628: 8, 832: 8, 836: 8, 863: 8, 865: 8, 866: 8, 867: 8, 868: 8, 869: 8, 870: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1070: 8, 1078: 8, 1080: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1177: 8, 1178: 8, 1179: 8, 1180: 8, 1182: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1243: 8, 1244: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1270: 8, 1271: 8, 1272: 8, 1274: 8, 1275: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1456: 8, 1479: 8
    }
  ],
}


FW_VERSIONS = {
  CAR.CX5: {
    (Ecu.eps, 0x730, None): [
      b'KJ01-3210X-G-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-M-00\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PYNF-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2G-188K2-D\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K123-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-E\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.esp, 0x760, None): [
      b'K123-437K2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KBJ5-437K2-B\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-N\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x88PYNC-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # HUD - Head Up Display
    (Ecu.hud, 0x7b2, None): [
      b'KB7W-55HK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # IC - Instrument Cluster
    (Ecu.combinationMeter, 0x720, None): [
      b'K157-554K2-V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # Air Bag
    (Ecu.srs, 0x737, None): [
      b'KB7W-57KK2-A2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # F_BCM - Front Body Control Module
    (Ecu.fbcm, 0x726, None): [
      b'TK52-675X2-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      ],
    # SSU - Start Stop Unit
    (Ecu.ssu, 0x731, None): [
      b'GMB6-675S1-A-05\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # R_BCM - Rear Body Control Module ?
    (Ecu.rbcm, 0x744, None): [
      b'B62W-675J1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # BSM - Blind Spot Monitoring ?
    (Ecu.bsm, 0x7c6, None): [
      b'\x01KB8C-67YK6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # AWD
    (Ecu.awd, 0x761, None): [
      b'SH9N-189K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    # Electrinic parking brake
    (Ecu.epb, 0x756, None): [
      b'K123-430K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    #
    (Ecu.unknown, 0x733, None): [
      b'K123-61190-0401-N5693\x00\x00\x00'
    ],
  },

  CAR.CX9 : {
    (Ecu.eps, 0x730, None): [
      b'KJ01-3210X-L-00\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PX23-188K2-B\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-B\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.esp, 0x760, None): [
      b'TN40-437K2-A\000\000\000\000\000\000\000\000\000\000\000\000',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-V\000\000\000\000\000\000\000\000\000\000\000\000',
    ]
  },

  CAR.Mazda3: {
    (Ecu.eps, 0x730, None): [
      b'K070-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'P5JD-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'B45A-437AS-0-08\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  }
}


DBC = {
  CAR.CX5: dbc_dict('mazda_2017', None),
  CAR.CX9: dbc_dict('mazda_2017', None),
  CAR.Mazda3: dbc_dict('mazda_2017', None),
}

GEN1 = [ CAR.CX5, CAR.CX9, CAR.Mazda3 ]
