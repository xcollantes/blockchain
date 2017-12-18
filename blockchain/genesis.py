# Xavier Collantes
# 12/17/2017
# File: snakecoin.py
# Experimentation with blockchain technology.  

import datetime as date

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")
