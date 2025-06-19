from blockchain import Blockchain

bc = Blockchain()
bc.add_transaction("Ngu", "Ngu hơn", 100)
bc.add_transaction("Bob", "Ngu hơn", 43)
proof = bc.proof_of_work(bc.get_previous_block().proof)
block = bc.add_block(proof)

for block in bc.chain:
    print("="*40)
    print(f"🔢 Block #{block.index}")
    print(f"⏰ Thời gian   : {block.timestamp}")
    print(f"🔐 Hash       : {block.hash}")
    print(f"🔗 Prev Hash  : {block.previous_hash}")
    print(f"📜 Proof      : {block.proof}")
    print(f"💼 Giao dịch  :")
    for tx in block.transactions:
        print(f"    {tx['sender']} → {tx['receiver']} : {tx['amount']} đơn vị")

