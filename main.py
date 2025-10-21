# main.py
import argparse
from db import run_find, run_aggregate
from llm import ask_llm_direct


schema="""{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "_id",
    "_class",
    "flightLegState"
  ],
  "properties": {
    "_id": {
      "type": "string"
    },
    "_class": {
      "type": "string"
    },
    "createdOn": {
      "$ref": "#/$defs/Date"
    },
    "flightLegState": {
      "type": "object",
      "required": [
        "annotations",
        "blockTimeActual",
        "blockTimeSch",
        "carrier",
        "codeShares",
        "crewConnections",
        "dateOfOrigin",
        "delays",
        "endCountry",
        "endStation",
        "endStationICAO",
        "endTimeOffset",
        "equipment",
        "flightHoursActual",
        "flightNumber",
        "flightStatus",
        "flightType",
        "handling",
        "isOTPAchieved",
        "isOTPConsidered",
        "isOTPFlight",
        "isOTTAchievedFlight",
        "isOTTFlight",
        "operation",
        "operationalStatus",
        "pax",
        "returnEvents",
        "scheduledEndTime",
        "scheduledStartTime",
        "seqNumber",
        "startCountry",
        "startStation",
        "startStationICAO",
        "startTimeOffset",
        "suffix",
        "taxiInTime",
        "taxiOutTime",
        "training",
        "turnTimeFlightAfter",
        "turnTimeFlightBeforeActual",
        "turnTimeFlightBeforeSch"
      ],
      "properties": {
        "annotations": {
          "type": "object",
          "required": [
            "annotation"
          ],
          "properties": {
            "annotation": {
              "type": "array",
              "items": {
                "type": "object",
                "required": [
                  "code",
                  "createdBy",
                  "creationTime",
                  "text"
                ],
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "createdBy": {
                    "type": "string"
                  },
                  "creationTime": {
                    "type": "string"
                  },
                  "modificationTime": {
                    "type": "string"
                  },
                  "modifiedBy": {
                    "type": "string"
                  },
                  "text": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "blockTimeActual": {
          "type": "string"
        },
        "blockTimeSch": {
          "type": "string"
        },
        "cancellationCode": {
          "type": "string"
        },
        "carrier": {
          "type": "string"
        }"""

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", required=True, help="User query in natural language")
    # parser.add_argument("--collection", required=True, help="MongoDB collection to query")
    # parser.add_argument("--limit", type=int, default=50, help="Number of docs to fetch")
    args = parser.parse_args()

    # Step 1: fetch data
    # data = run_find(args.collection, limit=args.limit)

    # Step 2: feed into LLM
    answer = ask_llm_direct(args.q, schema)

    # print("\n=== LLM Answer ===\n")
    print(answer)

if __name__ == "__main__":
    cli()
