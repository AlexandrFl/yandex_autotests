import kits

def test_create_kit_with_one_latter_in_forstname():
    kit = kits.createKits(kits.kit_1)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_1["name"]

def test_create_kit_with_511_latter_in_forstname():
    kit = kits.createKits(kits.kit_2)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_2["name"]

def test_create_kit_with_0_latter_in_forstname():
    kit = kits.createKits(kits.kit_3)
    assert kit.status_code == 400

def test_create_kit_with_512_latter_in_forstname():
    kit = kits.createKits(kits.kit_4)
    assert kit.status_code == 400

def test_create_kit_with_eng_latter_in_forstname():
    kit = kits.createKits(kits.kit_5)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_5["name"]

def test_create_kit_with_rus_latter_in_forstname():
    kit = kits.createKits(kits.kit_6)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_6["name"]

def test_create_kit_with_spec_latter_in_forstname():
    kit = kits.createKits(kits.kit_7)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_7["name"]

def test_create_kit_with_space_latter_in_forstname():
    kit = kits.createKits(kits.kit_8)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_8["name"]

def test_create_kit_with_num_latter_in_forstname():
    kit = kits.createKits(kits.kit_9)
    body = kit.json()["name"]
    assert kit.status_code == 201
    assert body == kits.kit_9["name"]

def test_create_kit_with_null_latter_in_forstname():
    kit = kits.createKits(kits.kit_10)
    assert kit.status_code == 400

def test_create_kit_with_wrong_tipe_latter_in_forstname():
    kit = kits.createKits(kits.kit_11)
    assert kit.status_code == 400