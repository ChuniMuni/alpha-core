from struct import pack

from utils.constants.OpCodes import *


class PacketWriter(object):
    @staticmethod
    def string_to_bytes(value):
        return value.encode('ascii') + b'\x00'

    @staticmethod
    def get_packet_format(opcode):
        if opcode != SMSG_AUTH_CHALLENGE:
            return '>' + 'B' * (4 if opcode == SMSG_AUTH_CHALLENGE else 6)

    @staticmethod
    def get_packet_header(opcode):
        # Packet header for SMSG_AUTH_CHALLENGE : Size: 2 bytes + Cmd: 2 bytes
        # Packet header : Size: 2 bytes + Cmd: 4 bytes
        if opcode == SMSG_AUTH_CHALLENGE:
            return 0, 0, int(opcode % 0x100), int(opcode / 0x100)
        else:
            return 0, 0, int(opcode % 0x100), int(opcode / 0x100), 0, 0
