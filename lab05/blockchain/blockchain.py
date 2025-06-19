from block import Block
import time
import hashlib


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), [], 1)
        self.chain.append(genesis_block)

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            check = hashlib.sha256(f'{new_proof**2 - previous_proof**2}'.encode()).hexdigest()
            if check[:4] == '0000':
                return new_proof
            new_proof += 1

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def add_block(self, proof):
        previous_block = self.get_previous_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_block.hash,
            timestamp=time.time(),
            transactions=self.transactions,
            proof=proof
        )
        self.transactions = []
        self.chain.append(new_block)
        return new_block
