import mogwai_hash
from binascii import unhexlify, hexlify

import unittest

# Mogwai block #1 Testnet
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockhash 1
# 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockheader 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b
# {
#   "hash": "00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b",
#   "confirmations": 1926,
#   "height": 1,
#   "version": 536870912,
#   "merkleroot": "486c457c7ce56305b0bb7205b4332bb3fa7eb97c7e9bc206a0063c651d0f0536",
#   "time": 1518804179,
#   "mediantime": 1518804179,
#   "nonce": 967123,
#   "bits": "1e0fffff",
#   "difficulty": 0.0002441371325370145,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200011",
#   "previousblockhash": "00000003c432c0f65db86e8ea6ae404a7e3af936c4c961359ce9eeec637cb901",
#   "nextblockhash": "000004f1e888ec21d342f5f5e65481f0fa2ea24373c7486c608b44f50e4e47ca"
# }
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockheader 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b false
# 0000002001b97c63eceee99c3561c9c436f93a7e4a40aea68e6eb85df6c032c40300000036050f1d653c06a006c29b7e7cb97efab32b33b40572bbb00563e57c7c456c48d31c875affff0f1ed3c10e00
               
header_hex = ("00000020" + # version
              "01b97c63eceee99c3561c9c436f93a7e4a40aea68e6eb85df6c032c403000000" + # previousblock            
              "36050f1d653c06a006c29b7e7cb97efab32b33b40572bbb00563e57c7c456c48" + # merkle
              "d31c875a" + # time 
              "ffff0f1e" + # bits
              "d3c10e00") # nonce
             
best_hash = '5be5aeeceb3a631dce3a440b35cd6b7e1bfc8ad6c7a6a28c04f537dd9d0e0000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_mogwai_hash(self):
        self.pow_hash = hexlify(mogwai_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

