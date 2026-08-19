def test_total_sums_items(cart):
    cart.add("book", 12000, 2)
    assert cart.total() == 24000

def test_first(cart):
    cart.add("book", 1000)
    assert len(cart.items) == 1

def test_second(cart):
    assert len(cart.items) == 0 # 새 장바구니를 기대

def test_save_report(tmp_path):
    f = tmp_path / "report.txt"
    f.write_text("매출 1000", encoding="utf-8")
    assert f.read_text(encoding="utf-8").startswith("매출")

def test_env(monkeypatch):
    monkeypatch.setenv("ENV", "test")
    import os
    assert os.getenv("ENV") == "test"