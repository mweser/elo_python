import base64

# import external_pb2

receipt = '5a2a1fd8'
receipt2 = 'CiIKIBRB19Uul7i2HivDzB8fMCOLbgAlnTq+cRbJF2KUSEI0EiIKIDhFYUymnMjt47yuEDj8x5zjsk402vyUMIgHPObC4gORGI/BNyI3CiIKICag6rwwgjGQ6Nm9zMol/2WEzaaLW5l3l6MX7pm4VK5LEcW6zicsFO8jGgiZG6Ak6hTstg=='


def b64_receipt_to_full_service_receipt(b64_string: str) -> dict:
    """Convert a b64-encoded protobuf Receipt into a full-service receipt object"""
    receipt_bytes = base64.b64decode(b64_string)
    # receipt = external_pb2.Receipt.FromString(receipt_bytes)
    #
    # full_service_receipt = {
    #     "object": "receiver_receipt",
    #     "public_key": receipt.public_key.SerializeToString().hex(),
    #     "confirmation": receipt.confirmation.SerializeToString().hex(),
    #     "tombstone_block": str(int(receipt.tombstone_block)),
    #     "amount": {
    #         "object": "amount",
    #         "commitment": receipt.amount.commitment.data.hex(),
    #         "masked_value": str(int(receipt.amount.masked_value)),
    #     },
    # }
    #
    # return full_service_receipt
    return receipt_bytes


print(b64_receipt_to_full_service_receipt(receipt2))
