import pytest
from phantasyRestClient import MachinePortalResources as mp_res


def test_getLattice():
    assert mp_res.getLattice() == {'machine': 'FRIB', 'segment': 'LINAC'}


def test_getElements():
    """Get all elements, *F1S1*, QUAD"""
    r = mp_res.getElements(name_pattern="*F1S1*", type_pattern="QUAD")
    assert r == [['FS_F1S1:Q_D1013'], ['FS_F1S1:Q_D1024'], ['FS_F1S1:Q_D1035'],
                 ['FS_F1S1:Q_D1137'], ['FS_F1S1:Q_D1148'], ['FS_F1S1:Q_D1170']]


def test_getElemPos():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemPos1(name) == 0.988163
    assert mp_res.getElemPos2(name) == 1.611836
    assert mp_res.getElemPos(name) == [(0.988163, 1.611836)]


def test_getElemType():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemType(name) == "QUAD"


def test_getElemTypeAlias():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemTypeAlias(name) == "QUAD_FSQ1"


def test_getElemNameAlias():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemNameAlias(name) == "RT quadrupole"


def test_getElemFields():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemFields(name) == [[
        'I', 'B2', 'B', 'L', 'PWRSTS', 'POWER_STATUS'
    ]]


def test_getElemPVs():
    name = "FS_F1S1:Q_D1013"
    assert mp_res.getElemPVs(name, "I",
                             "readback") == [['FS_F1S1:PSQ_D1013:I_RD']]
    assert mp_res.getElemPVs(name, "I",
                             "setpoint") == [['FS_F1S1:PSQ_D1013:I_CSET']]


def test_convert():
    name = "FS_F1S1:Q_D1013"
    b2_100 = mp_res.convert(name, 100, "I", "B2")
    assert b2_100 == 1.50683
    assert mp_res.convert(name, b2_100, "B2", "I") == 100


def test_calcEnergyLoss():
    p = {"A": 238, "Z": 92, "Ek": 1000}
    m = {"A": 63.546, "Z": 29, "thickness": 1000}
    r = mp_res.calcEnergyLoss(p, m)
    r0 = {
        'dE/dx': 14.518020957575775,
        'Ek': 938.6732788085938,
        'Ek_std': 0.28671697408211333,
        'range_in': 12592.18308165448,
        'range_out': 11592.183580096036,
        'range_std': 11.897422600402564,
        'angle_std': 1.0526343248784542,
        'q_in': 91.76187896728516,
        'q_out': 91.74201965332031
    }
    assert r == r0


def test_calcEnergyLossList():
    p = {"A": 238, "Z": 92, "Ek": 1000}
    m = {"A": 63.546, "Z": 29, "thickness": 1000}
    r = mp_res.calcEnergyLossList(p, m)
    r0 = [
        938.6732788085938,
        14.518020957575775,
        0.28671697408211333,
        12592.18308165448,
        11592.183580096036,
        11.897422600402564,
        1.0526343248784542,
        91.76187896728516,
        91.74201965332031
        ]
    assert r == r0
