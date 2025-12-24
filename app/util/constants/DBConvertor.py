BE_PROJECTS = {
    "CVWritingSupporter Backend": {
        "Database Design": {
            "Requirement & GAP Analysis": {
                "Review Existing CV Data Sources": {
                    "start": "start_1",
                    "dead": "dead_1"
                },
                "Identify Missing CV Attributes": {
                    "start": "start_2",
                    "dead": "dead_2"
                },
                "Map Business Fields to Database Columns": {
                    "start": "start_3",
                    "dead": "dead_3"
                },
                "Validate Data Ownership Rules": {
                    "start": "start_4",
                    "dead": "dead_4"
                },
                "Approve Database Scope with Stakeholders": {
                    "start": "start_5",
                    "dead": "dead_5"
                },
                "Define User–CV Relationship Model": {
                    "start": "start_6",
                    "dead": "dead_6"
                },
                "Design CV Versioning Strategy": {
                    "start": "start_7",
                    "dead": "dead_7"
                },
                "Review GDPR & PII Constraints": {
                    "start": "start_8",
                    "dead": "dead_8"
                },
                "Finalize Database Requirement Specification": {
                    "start": "start_9",
                    "dead": "dead_9"
                },
                "Sign Off Database Design Phase": {
                    "start": "start_10",
                    "dead": "dead_10"
                }
            },
            "Schema & Modeling": {
                "Design Core User Tables": {
                    "start": "start_11",
                    "dead": "dead_11"
                },
                "Design CV Metadata Tables": {
                    "start": "start_12",
                    "dead": "dead_12"
                },
                "Design Skill & Experience Tables": {
                    "start": "start_13",
                    "dead": "dead_13"
                },
                "Design CV Scoring Tables": {
                    "start": "start_14",
                    "dead": "dead_14"
                },
                "Model One-to-Many CV Relationships": {
                    "start": "start_15",
                    "dead": "dead_15"
                },
                "Review ER Diagram with Backend Team": {
                    "start": "start_16",
                    "dead": "dead_16"
                },
                "Apply Normalization Rules": {
                    "start": "start_17",
                    "dead": "dead_17"
                },
                "Decide Controlled Denormalization": {
                    "start": "start_18",
                    "dead": "dead_18"
                },
                "Finalize Logical Schema": {
                    "start": "start_19",
                    "dead": "dead_19"
                },
                "Prepare Physical Schema Draft": {
                    "start": "start_20",
                    "dead": "dead_20"
                }
            }
        },
        "Build Infrastructure": {
            "Environment Preparation": {
                "Initialize Backend Repository Structure": {
                    "start": "start_21",
                    "dead": "dead_21"
                },
                "Set Up Local Development Environment": {
                    "start": "start_22",
                    "dead": "dead_22"
                },
                "Configure Environment Variables": {
                    "start": "start_23",
                    "dead": "dead_23"
                },
                "Prepare Staging Configuration": {
                    "start": "start_24",
                    "dead": "dead_24"
                },
                "Align Environment Naming Convention": {
                    "start": "start_25",
                    "dead": "dead_25"
                },
                "Validate Environment Isolation": {
                    "start": "start_26",
                    "dead": "dead_26"
                },
                "Review Deployment Readiness": {
                    "start": "start_27",
                    "dead": "dead_27"
                },
                "Approve Infrastructure Baseline": {
                    "start": "start_28",
                    "dead": "dead_28"
                }
            },
            "CI/CD & Deployment": {
                "Design Continuous Integration Workflow": {
                    "start": "start_29",
                    "dead": "dead_29"
                },
                "Configure Automated Test Pipeline": {
                    "start": "start_30",
                    "dead": "dead_30"
                },
                "Set Up Artifact Storage": {
                    "start": "start_31",
                    "dead": "dead_31"
                },
                "Design Deployment Strategy": {
                    "start": "start_32",
                    "dead": "dead_32"
                },
                "Implement Continuous Deployment": {
                    "start": "start_33",
                    "dead": "dead_33"
                },
                "Validate Rollback Mechanism": {
                    "start": "start_34",
                    "dead": "dead_34"
                },
                "Document Deployment Process": {
                    "start": "start_35",
                    "dead": "dead_35"
                },
                "Handover CI/CD to Team": {
                    "start": "start_36",
                    "dead": "dead_36"
                }
            }
        },
        "Main Backend Services": {
            "User & Identity Services": {
                "Implement User Registration API": {
                    "start": "start_37",
                    "dead": "dead_37"
                },
                "Implement Login & Logout API": {
                    "start": "start_38",
                    "dead": "dead_38"
                },
                "Integrate Token-Based Authentication": {
                    "start": "start_39",
                    "dead": "dead_39"
                },
                "Handle Password Encryption": {
                    "start": "start_40",
                    "dead": "dead_40"
                },
                "Implement Refresh Token Flow": {
                    "start": "start_41",
                    "dead": "dead_41"
                },
                "Audit Authentication Logic": {
                    "start": "start_42",
                    "dead": "dead_42"
                },
                "Document Identity Service APIs": {
                    "start": "start_43",
                    "dead": "dead_43"
                },
                "Stabilize User Authentication Module": {
                    "start": "start_44",
                    "dead": "dead_44"
                }
            },
            "CV Processing & Analysis": {
                "Parse Uploaded CV File": {
                    "start": "start_45",
                    "dead": "dead_45"
                },
                "Extract Structured CV Data": {
                    "start": "start_46",
                    "dead": "dead_46"
                },
                "Normalize Skill Information": {
                    "start": "start_47",
                    "dead": "dead_47"
                },
                "Analyze Work Experience Sections": {
                    "start": "start_48",
                    "dead": "dead_48"
                },
                "Evaluate Education Background": {
                    "start": "start_49",
                    "dead": "dead_49"
                },
                "Detect Missing CV Sections": {
                    "start": "start_50",
                    "dead": "dead_50"
                },
                "Generate CV Quality Metrics": {
                    "start": "start_51",
                    "dead": "dead_51"
                },
                "Prepare CV Analysis Output": {
                    "start": "start_52",
                    "dead": "dead_52"
                }
            },
            "Recommendation & Scoring": {
                "Define CV Scoring Criteria": {
                    "start": "start_53",
                    "dead": "dead_53"
                },
                "Implement Rule-Based Scoring Engine": {
                    "start": "start_54",
                    "dead": "dead_54"
                },
                "Integrate AI Recommendation Model": {
                    "start": "start_55",
                    "dead": "dead_55"
                },
                "Optimize Scoring Performance": {
                    "start": "start_56",
                    "dead": "dead_56"
                },
                "Validate Recommendation Accuracy": {
                    "start": "start_57",
                    "dead": "dead_57"
                },
                "Log Recommendation Decisions": {
                    "start": "start_58",
                    "dead": "dead_58"
                },
                "Expose Recommendation API": {
                    "start": "start_59",
                    "dead": "dead_59"
                },
                "Finalize Recommendation Module": {
                    "start": "start_60",
                    "dead": "dead_60"
                }
            }
        },
        "Refactor Backend Services": {
            "Codebase Restructuring": {
                "Analyze Technical Debt Areas": {
                    "start": "start_61",
                    "dead": "dead_61"
                },
                "Refactor Service Layer Boundaries": {
                    "start": "start_62",
                    "dead": "dead_62"
                },
                "Standardize Project Package Structure": {
                    "start": "start_63",
                    "dead": "dead_63"
                },
                "Remove Deprecated Components": {
                    "start": "start_64",
                    "dead": "dead_64"
                },
                "Improve Dependency Management": {
                    "start": "start_65",
                    "dead": "dead_65"
                },
                "Align Code with Architecture Guidelines": {
                    "start": "start_66",
                    "dead": "dead_66"
                },
                "Review Refactored Modules": {
                    "start": "start_67",
                    "dead": "dead_67"
                },
                "Approve Refactor Completion": {
                    "start": "start_68",
                    "dead": "dead_68"
                }
            },
            "Performance & Stability": {
                "Identify Performance Bottlenecks": {
                    "start": "start_69",
                    "dead": "dead_69"
                },
                "Optimize Heavy Database Queries": {
                    "start": "start_70",
                    "dead": "dead_70"
                },
                "Reduce API Payload Size": {
                    "start": "start_71",
                    "dead": "dead_71"
                },
                "Improve Caching Strategy": {
                    "start": "start_72",
                    "dead": "dead_72"
                },
                "Stabilize Concurrent Request Handling": {
                    "start": "start_73",
                    "dead": "dead_73"
                },
                "Fix Memory Consumption Issues": {
                    "start": "start_74",
                    "dead": "dead_74"
                },
                "Re-test High Load Scenarios": {
                    "start": "start_75",
                    "dead": "dead_75"
                },
                "Confirm Performance Targets Met": {
                    "start": "start_76",
                    "dead": "dead_76"
                }
            }
        },
        "Backend Operational Hardening": {
            "Operational Improvements Batch 9": {
                "Operational Improvement Task 77": {
                    "start": "start_77",
                    "dead": "dead_77"
                },
                "Operational Improvement Task 78": {
                    "start": "start_78",
                    "dead": "dead_78"
                },
                "Operational Improvement Task 79": {
                    "start": "start_79",
                    "dead": "dead_79"
                },
                "Operational Improvement Task 80": {
                    "start": "start_80",
                    "dead": "dead_80"
                },
                "Operational Improvement Task 81": {
                    "start": "start_81",
                    "dead": "dead_81"
                },
                "Operational Improvement Task 82": {
                    "start": "start_82",
                    "dead": "dead_82"
                },
                "Operational Improvement Task 83": {
                    "start": "start_83",
                    "dead": "dead_83"
                },
                "Operational Improvement Task 84": {
                    "start": "start_84",
                    "dead": "dead_84"
                }
            },
            "Operational Improvements Batch 10": {
                "Operational Improvement Task 85": {
                    "start": "start_85",
                    "dead": "dead_85"
                },
                "Operational Improvement Task 86": {
                    "start": "start_86",
                    "dead": "dead_86"
                },
                "Operational Improvement Task 87": {
                    "start": "start_87",
                    "dead": "dead_87"
                },
                "Operational Improvement Task 88": {
                    "start": "start_88",
                    "dead": "dead_88"
                },
                "Operational Improvement Task 89": {
                    "start": "start_89",
                    "dead": "dead_89"
                },
                "Operational Improvement Task 90": {
                    "start": "start_90",
                    "dead": "dead_90"
                },
                "Operational Improvement Task 91": {
                    "start": "start_91",
                    "dead": "dead_91"
                },
                "Operational Improvement Task 92": {
                    "start": "start_92",
                    "dead": "dead_92"
                }
            },
            "Operational Improvements Batch 11": {
                "Operational Improvement Task 93": {
                    "start": "start_93",
                    "dead": "dead_93"
                },
                "Operational Improvement Task 94": {
                    "start": "start_94",
                    "dead": "dead_94"
                },
                "Operational Improvement Task 95": {
                    "start": "start_95",
                    "dead": "dead_95"
                },
                "Operational Improvement Task 96": {
                    "start": "start_96",
                    "dead": "dead_96"
                },
                "Operational Improvement Task 97": {
                    "start": "start_97",
                    "dead": "dead_97"
                },
                "Operational Improvement Task 98": {
                    "start": "start_98",
                    "dead": "dead_98"
                },
                "Operational Improvement Task 99": {
                    "start": "start_99",
                    "dead": "dead_99"
                },
                "Operational Improvement Task 100": {
                    "start": "start_100",
                    "dead": "dead_100"
                }
            },
            "Operational Improvements Batch 12": {
                "Operational Improvement Task 101": {
                    "start": "start_101",
                    "dead": "dead_101"
                },
                "Operational Improvement Task 102": {
                    "start": "start_102",
                    "dead": "dead_102"
                },
                "Operational Improvement Task 103": {
                    "start": "start_103",
                    "dead": "dead_103"
                },
                "Operational Improvement Task 104": {
                    "start": "start_104",
                    "dead": "dead_104"
                },
                "Operational Improvement Task 105": {
                    "start": "start_105",
                    "dead": "dead_105"
                },
                "Operational Improvement Task 106": {
                    "start": "start_106",
                    "dead": "dead_106"
                },
                "Operational Improvement Task 107": {
                    "start": "start_107",
                    "dead": "dead_107"
                },
                "Operational Improvement Task 108": {
                    "start": "start_108",
                    "dead": "dead_108"
                }
            },
            "Operational Improvements Batch 13": {
                "Operational Improvement Task 109": {
                    "start": "start_109",
                    "dead": "dead_109"
                },
                "Operational Improvement Task 110": {
                    "start": "start_110",
                    "dead": "dead_110"
                },
                "Operational Improvement Task 111": {
                    "start": "start_111",
                    "dead": "dead_111"
                },
                "Operational Improvement Task 112": {
                    "start": "start_112",
                    "dead": "dead_112"
                },
                "Operational Improvement Task 113": {
                    "start": "start_113",
                    "dead": "dead_113"
                },
                "Operational Improvement Task 114": {
                    "start": "start_114",
                    "dead": "dead_114"
                },
                "Operational Improvement Task 115": {
                    "start": "start_115",
                    "dead": "dead_115"
                },
                "Operational Improvement Task 116": {
                    "start": "start_116",
                    "dead": "dead_116"
                }
            },
            "Operational Improvements Batch 14": {
                "Operational Improvement Task 117": {
                    "start": "start_117",
                    "dead": "dead_117"
                },
                "Operational Improvement Task 118": {
                    "start": "start_118",
                    "dead": "dead_118"
                },
                "Operational Improvement Task 119": {
                    "start": "start_119",
                    "dead": "dead_119"
                },
                "Operational Improvement Task 120": {
                    "start": "start_120",
                    "dead": "dead_120"
                },
                "Operational Improvement Task 121": {
                    "start": "start_121",
                    "dead": "dead_121"
                },
                "Operational Improvement Task 122": {
                    "start": "start_122",
                    "dead": "dead_122"
                },
                "Operational Improvement Task 123": {
                    "start": "start_123",
                    "dead": "dead_123"
                },
                "Operational Improvement Task 124": {
                    "start": "start_124",
                    "dead": "dead_124"
                }
            },
            "Operational Improvements Batch 15": {
                "Operational Improvement Task 125": {
                    "start": "start_125",
                    "dead": "dead_125"
                },
                "Operational Improvement Task 126": {
                    "start": "start_126",
                    "dead": "dead_126"
                },
                "Operational Improvement Task 127": {
                    "start": "start_127",
                    "dead": "dead_127"
                },
                "Operational Improvement Task 128": {
                    "start": "start_128",
                    "dead": "dead_128"
                },
                "Operational Improvement Task 129": {
                    "start": "start_129",
                    "dead": "dead_129"
                },
                "Operational Improvement Task 130": {
                    "start": "start_130",
                    "dead": "dead_130"
                },
                "Operational Improvement Task 131": {
                    "start": "start_131",
                    "dead": "dead_131"
                },
                "Operational Improvement Task 132": {
                    "start": "start_132",
                    "dead": "dead_132"
                }
            },
            "Operational Improvements Batch 16": {
                "Operational Improvement Task 133": {
                    "start": "start_133",
                    "dead": "dead_133"
                },
                "Operational Improvement Task 134": {
                    "start": "start_134",
                    "dead": "dead_134"
                },
                "Operational Improvement Task 135": {
                    "start": "start_135",
                    "dead": "dead_135"
                },
                "Operational Improvement Task 136": {
                    "start": "start_136",
                    "dead": "dead_136"
                },
                "Operational Improvement Task 137": {
                    "start": "start_137",
                    "dead": "dead_137"
                },
                "Operational Improvement Task 138": {
                    "start": "start_138",
                    "dead": "dead_138"
                },
                "Operational Improvement Task 139": {
                    "start": "start_139",
                    "dead": "dead_139"
                },
                "Operational Improvement Task 140": {
                    "start": "start_140",
                    "dead": "dead_140"
                }
            },
            "Operational Improvements Batch 17": {
                "Operational Improvement Task 141": {
                    "start": "start_141",
                    "dead": "dead_141"
                },
                "Operational Improvement Task 142": {
                    "start": "start_142",
                    "dead": "dead_142"
                },
                "Operational Improvement Task 143": {
                    "start": "start_143",
                    "dead": "dead_143"
                },
                "Operational Improvement Task 144": {
                    "start": "start_144",
                    "dead": "dead_144"
                },
                "Operational Improvement Task 145": {
                    "start": "start_145",
                    "dead": "dead_145"
                },
                "Operational Improvement Task 146": {
                    "start": "start_146",
                    "dead": "dead_146"
                },
                "Operational Improvement Task 147": {
                    "start": "start_147",
                    "dead": "dead_147"
                },
                "Operational Improvement Task 148": {
                    "start": "start_148",
                    "dead": "dead_148"
                }
            },
            "Operational Improvements Batch 18": {
                "Operational Improvement Task 149": {
                    "start": "start_149",
                    "dead": "dead_149"
                },
                "Operational Improvement Task 150": {
                    "start": "start_150",
                    "dead": "dead_150"
                },
                "Operational Improvement Task 151": {
                    "start": "start_151",
                    "dead": "dead_151"
                },
                "Operational Improvement Task 152": {
                    "start": "start_152",
                    "dead": "dead_152"
                },
                "Operational Improvement Task 153": {
                    "start": "start_153",
                    "dead": "dead_153"
                },
                "Operational Improvement Task 154": {
                    "start": "start_154",
                    "dead": "dead_154"
                },
                "Operational Improvement Task 155": {
                    "start": "start_155",
                    "dead": "dead_155"
                },
                "Operational Improvement Task 156": {
                    "start": "start_156",
                    "dead": "dead_156"
                }
            },
            "Operational Improvements Batch 19": {
                "Operational Improvement Task 157": {
                    "start": "start_157",
                    "dead": "dead_157"
                },
                "Operational Improvement Task 158": {
                    "start": "start_158",
                    "dead": "dead_158"
                },
                "Operational Improvement Task 159": {
                    "start": "start_159",
                    "dead": "dead_159"
                },
                "Operational Improvement Task 160": {
                    "start": "start_160",
                    "dead": "dead_160"
                },
                "Operational Improvement Task 161": {
                    "start": "start_161",
                    "dead": "dead_161"
                },
                "Operational Improvement Task 162": {
                    "start": "start_162",
                    "dead": "dead_162"
                },
                "Operational Improvement Task 163": {
                    "start": "start_163",
                    "dead": "dead_163"
                },
                "Operational Improvement Task 164": {
                    "start": "start_164",
                    "dead": "dead_164"
                }
            },
            "Operational Improvements Batch 20": {
                "Operational Improvement Task 165": {
                    "start": "start_165",
                    "dead": "dead_165"
                },
                "Operational Improvement Task 166": {
                    "start": "start_166",
                    "dead": "dead_166"
                },
                "Operational Improvement Task 167": {
                    "start": "start_167",
                    "dead": "dead_167"
                },
                "Operational Improvement Task 168": {
                    "start": "start_168",
                    "dead": "dead_168"
                },
                "Operational Improvement Task 169": {
                    "start": "start_169",
                    "dead": "dead_169"
                },
                "Operational Improvement Task 170": {
                    "start": "start_170",
                    "dead": "dead_170"
                },
                "Operational Improvement Task 171": {
                    "start": "start_171",
                    "dead": "dead_171"
                },
                "Operational Improvement Task 172": {
                    "start": "start_172",
                    "dead": "dead_172"
                }
            },
            "Operational Improvements Batch 21": {
                "Operational Improvement Task 173": {
                    "start": "start_173",
                    "dead": "dead_173"
                },
                "Operational Improvement Task 174": {
                    "start": "start_174",
                    "dead": "dead_174"
                },
                "Operational Improvement Task 175": {
                    "start": "start_175",
                    "dead": "dead_175"
                },
                "Operational Improvement Task 176": {
                    "start": "start_176",
                    "dead": "dead_176"
                },
                "Operational Improvement Task 177": {
                    "start": "start_177",
                    "dead": "dead_177"
                },
                "Operational Improvement Task 178": {
                    "start": "start_178",
                    "dead": "dead_178"
                },
                "Operational Improvement Task 179": {
                    "start": "start_179",
                    "dead": "dead_179"
                },
                "Operational Improvement Task 180": {
                    "start": "start_180",
                    "dead": "dead_180"
                }
            },
            "Operational Improvements Batch 22": {
                "Operational Improvement Task 181": {
                    "start": "start_181",
                    "dead": "dead_181"
                },
                "Operational Improvement Task 182": {
                    "start": "start_182",
                    "dead": "dead_182"
                },
                "Operational Improvement Task 183": {
                    "start": "start_183",
                    "dead": "dead_183"
                },
                "Operational Improvement Task 184": {
                    "start": "start_184",
                    "dead": "dead_184"
                },
                "Operational Improvement Task 185": {
                    "start": "start_185",
                    "dead": "dead_185"
                },
                "Operational Improvement Task 186": {
                    "start": "start_186",
                    "dead": "dead_186"
                },
                "Operational Improvement Task 187": {
                    "start": "start_187",
                    "dead": "dead_187"
                },
                "Operational Improvement Task 188": {
                    "start": "start_188",
                    "dead": "dead_188"
                }
            },
            "Operational Improvements Batch 23": {
                "Operational Improvement Task 189": {
                    "start": "start_189",
                    "dead": "dead_189"
                },
                "Operational Improvement Task 190": {
                    "start": "start_190",
                    "dead": "dead_190"
                },
                "Operational Improvement Task 191": {
                    "start": "start_191",
                    "dead": "dead_191"
                },
                "Operational Improvement Task 192": {
                    "start": "start_192",
                    "dead": "dead_192"
                },
                "Operational Improvement Task 193": {
                    "start": "start_193",
                    "dead": "dead_193"
                },
                "Operational Improvement Task 194": {
                    "start": "start_194",
                    "dead": "dead_194"
                },
                "Operational Improvement Task 195": {
                    "start": "start_195",
                    "dead": "dead_195"
                },
                "Operational Improvement Task 196": {
                    "start": "start_196",
                    "dead": "dead_196"
                }
            },
            "Operational Improvements Batch 24": {
                "Operational Improvement Task 197": {
                    "start": "start_197",
                    "dead": "dead_197"
                },
                "Operational Improvement Task 198": {
                    "start": "start_198",
                    "dead": "dead_198"
                },
                "Operational Improvement Task 199": {
                    "start": "start_199",
                    "dead": "dead_199"
                },
                "Operational Improvement Task 200": {
                    "start": "start_200",
                    "dead": "dead_200"
                },
                "Operational Improvement Task 201": {
                    "start": "start_201",
                    "dead": "dead_201"
                },
                "Operational Improvement Task 202": {
                    "start": "start_202",
                    "dead": "dead_202"
                },
                "Operational Improvement Task 203": {
                    "start": "start_203",
                    "dead": "dead_203"
                },
                "Operational Improvement Task 204": {
                    "start": "start_204",
                    "dead": "dead_204"
                }
            },
            "Operational Improvements Batch 25": {
                "Operational Improvement Task 205": {
                    "start": "start_205",
                    "dead": "dead_205"
                },
                "Operational Improvement Task 206": {
                    "start": "start_206",
                    "dead": "dead_206"
                },
                "Operational Improvement Task 207": {
                    "start": "start_207",
                    "dead": "dead_207"
                },
                "Operational Improvement Task 208": {
                    "start": "start_208",
                    "dead": "dead_208"
                },
                "Operational Improvement Task 209": {
                    "start": "start_209",
                    "dead": "dead_209"
                },
                "Operational Improvement Task 210": {
                    "start": "start_210",
                    "dead": "dead_210"
                },
                "Operational Improvement Task 211": {
                    "start": "start_211",
                    "dead": "dead_211"
                },
                "Operational Improvement Task 212": {
                    "start": "start_212",
                    "dead": "dead_212"
                }
            },
            "Operational Improvements Batch 26": {
                "Operational Improvement Task 213": {
                    "start": "start_213",
                    "dead": "dead_213"
                },
                "Operational Improvement Task 214": {
                    "start": "start_214",
                    "dead": "dead_214"
                },
                "Operational Improvement Task 215": {
                    "start": "start_215",
                    "dead": "dead_215"
                },
                "Operational Improvement Task 216": {
                    "start": "start_216",
                    "dead": "dead_216"
                },
                "Operational Improvement Task 217": {
                    "start": "start_217",
                    "dead": "dead_217"
                },
                "Operational Improvement Task 218": {
                    "start": "start_218",
                    "dead": "dead_218"
                },
                "Operational Improvement Task 219": {
                    "start": "start_219",
                    "dead": "dead_219"
                },
                "Operational Improvement Task 220": {
                    "start": "start_220",
                    "dead": "dead_220"
                }
            },
            "Operational Improvements Batch 27": {
                "Operational Improvement Task 221": {
                    "start": "start_221",
                    "dead": "dead_221"
                },
                "Operational Improvement Task 222": {
                    "start": "start_222",
                    "dead": "dead_222"
                },
                "Operational Improvement Task 223": {
                    "start": "start_223",
                    "dead": "dead_223"
                },
                "Operational Improvement Task 224": {
                    "start": "start_224",
                    "dead": "dead_224"
                },
                "Operational Improvement Task 225": {
                    "start": "start_225",
                    "dead": "dead_225"
                },
                "Operational Improvement Task 226": {
                    "start": "start_226",
                    "dead": "dead_226"
                },
                "Operational Improvement Task 227": {
                    "start": "start_227",
                    "dead": "dead_227"
                },
                "Operational Improvement Task 228": {
                    "start": "start_228",
                    "dead": "dead_228"
                }
            },
            "Operational Improvements Batch 28": {
                "Operational Improvement Task 229": {
                    "start": "start_229",
                    "dead": "dead_229"
                },
                "Operational Improvement Task 230": {
                    "start": "start_230",
                    "dead": "dead_230"
                },
                "Operational Improvement Task 231": {
                    "start": "start_231",
                    "dead": "dead_231"
                },
                "Operational Improvement Task 232": {
                    "start": "start_232",
                    "dead": "dead_232"
                },
                "Operational Improvement Task 233": {
                    "start": "start_233",
                    "dead": "dead_233"
                },
                "Operational Improvement Task 234": {
                    "start": "start_234",
                    "dead": "dead_234"
                },
                "Operational Improvement Task 235": {
                    "start": "start_235",
                    "dead": "dead_235"
                },
                "Operational Improvement Task 236": {
                    "start": "start_236",
                    "dead": "dead_236"
                }
            },
            "Operational Improvements Batch 29": {
                "Operational Improvement Task 237": {
                    "start": "start_237",
                    "dead": "dead_237"
                },
                "Operational Improvement Task 238": {
                    "start": "start_238",
                    "dead": "dead_238"
                },
                "Operational Improvement Task 239": {
                    "start": "start_239",
                    "dead": "dead_239"
                },
                "Operational Improvement Task 240": {
                    "start": "start_240",
                    "dead": "dead_240"
                },
                "Operational Improvement Task 241": {
                    "start": "start_241",
                    "dead": "dead_241"
                },
                "Operational Improvement Task 242": {
                    "start": "start_242",
                    "dead": "dead_242"
                },
                "Operational Improvement Task 243": {
                    "start": "start_243",
                    "dead": "dead_243"
                },
                "Operational Improvement Task 244": {
                    "start": "start_244",
                    "dead": "dead_244"
                }
            },
            "Operational Improvements Batch 30": {
                "Operational Improvement Task 245": {
                    "start": "start_245",
                    "dead": "dead_245"
                },
                "Operational Improvement Task 246": {
                    "start": "start_246",
                    "dead": "dead_246"
                },
                "Operational Improvement Task 247": {
                    "start": "start_247",
                    "dead": "dead_247"
                },
                "Operational Improvement Task 248": {
                    "start": "start_248",
                    "dead": "dead_248"
                },
                "Operational Improvement Task 249": {
                    "start": "start_249",
                    "dead": "dead_249"
                },
                "Operational Improvement Task 250": {
                    "start": "start_250",
                    "dead": "dead_250"
                },
                "Operational Improvement Task 251": {
                    "start": "start_251",
                    "dead": "dead_251"
                },
                "Operational Improvement Task 252": {
                    "start": "start_252",
                    "dead": "dead_252"
                }
            },
            "Operational Improvements Batch 31": {
                "Operational Improvement Task 253": {
                    "start": "start_253",
                    "dead": "dead_253"
                },
                "Operational Improvement Task 254": {
                    "start": "start_254",
                    "dead": "dead_254"
                },
                "Operational Improvement Task 255": {
                    "start": "start_255",
                    "dead": "dead_255"
                },
                "Operational Improvement Task 256": {
                    "start": "start_256",
                    "dead": "dead_256"
                },
                "Operational Improvement Task 257": {
                    "start": "start_257",
                    "dead": "dead_257"
                },
                "Operational Improvement Task 258": {
                    "start": "start_258",
                    "dead": "dead_258"
                },
                "Operational Improvement Task 259": {
                    "start": "start_259",
                    "dead": "dead_259"
                },
                "Operational Improvement Task 260": {
                    "start": "start_260",
                    "dead": "dead_260"
                }
            },
            "Operational Improvements Batch 32": {
                "Operational Improvement Task 261": {
                    "start": "start_261",
                    "dead": "dead_261"
                },
                "Operational Improvement Task 262": {
                    "start": "start_262",
                    "dead": "dead_262"
                },
                "Operational Improvement Task 263": {
                    "start": "start_263",
                    "dead": "dead_263"
                },
                "Operational Improvement Task 264": {
                    "start": "start_264",
                    "dead": "dead_264"
                },
                "Operational Improvement Task 265": {
                    "start": "start_265",
                    "dead": "dead_265"
                },
                "Operational Improvement Task 266": {
                    "start": "start_266",
                    "dead": "dead_266"
                },
                "Operational Improvement Task 267": {
                    "start": "start_267",
                    "dead": "dead_267"
                },
                "Operational Improvement Task 268": {
                    "start": "start_268",
                    "dead": "dead_268"
                }
            },
            "Operational Improvements Batch 33": {
                "Operational Improvement Task 269": {
                    "start": "start_269",
                    "dead": "dead_269"
                },
                "Operational Improvement Task 270": {
                    "start": "start_270",
                    "dead": "dead_270"
                },
                "Operational Improvement Task 271": {
                    "start": "start_271",
                    "dead": "dead_271"
                },
                "Operational Improvement Task 272": {
                    "start": "start_272",
                    "dead": "dead_272"
                },
                "Operational Improvement Task 273": {
                    "start": "start_273",
                    "dead": "dead_273"
                },
                "Operational Improvement Task 274": {
                    "start": "start_274",
                    "dead": "dead_274"
                },
                "Operational Improvement Task 275": {
                    "start": "start_275",
                    "dead": "dead_275"
                },
                "Operational Improvement Task 276": {
                    "start": "start_276",
                    "dead": "dead_276"
                }
            },
            "Operational Improvements Batch 34": {
                "Operational Improvement Task 277": {
                    "start": "start_277",
                    "dead": "dead_277"
                },
                "Operational Improvement Task 278": {
                    "start": "start_278",
                    "dead": "dead_278"
                },
                "Operational Improvement Task 279": {
                    "start": "start_279",
                    "dead": "dead_279"
                },
                "Operational Improvement Task 280": {
                    "start": "start_280",
                    "dead": "dead_280"
                },
                "Operational Improvement Task 281": {
                    "start": "start_281",
                    "dead": "dead_281"
                },
                "Operational Improvement Task 282": {
                    "start": "start_282",
                    "dead": "dead_282"
                },
                "Operational Improvement Task 283": {
                    "start": "start_283",
                    "dead": "dead_283"
                },
                "Operational Improvement Task 284": {
                    "start": "start_284",
                    "dead": "dead_284"
                }
            },
            "Operational Improvements Batch 35": {
                "Operational Improvement Task 285": {
                    "start": "start_285",
                    "dead": "dead_285"
                },
                "Operational Improvement Task 286": {
                    "start": "start_286",
                    "dead": "dead_286"
                },
                "Operational Improvement Task 287": {
                    "start": "start_287",
                    "dead": "dead_287"
                },
                "Operational Improvement Task 288": {
                    "start": "start_288",
                    "dead": "dead_288"
                },
                "Operational Improvement Task 289": {
                    "start": "start_289",
                    "dead": "dead_289"
                },
                "Operational Improvement Task 290": {
                    "start": "start_290",
                    "dead": "dead_290"
                },
                "Operational Improvement Task 291": {
                    "start": "start_291",
                    "dead": "dead_291"
                },
                "Operational Improvement Task 292": {
                    "start": "start_292",
                    "dead": "dead_292"
                }
            },
            "Operational Improvements Batch 36": {
                "Operational Improvement Task 293": {
                    "start": "start_293",
                    "dead": "dead_293"
                },
                "Operational Improvement Task 294": {
                    "start": "start_294",
                    "dead": "dead_294"
                },
                "Operational Improvement Task 295": {
                    "start": "start_295",
                    "dead": "dead_295"
                },
                "Operational Improvement Task 296": {
                    "start": "start_296",
                    "dead": "dead_296"
                },
                "Operational Improvement Task 297": {
                    "start": "start_297",
                    "dead": "dead_297"
                },
                "Operational Improvement Task 298": {
                    "start": "start_298",
                    "dead": "dead_298"
                },
                "Operational Improvement Task 299": {
                    "start": "start_299",
                    "dead": "dead_299"
                },
                "Operational Improvement Task 300": {
                    "start": "start_300",
                    "dead": "dead_300"
                }
            },
            "Operational Improvements Batch 37": {
                "Operational Improvement Task 301": {
                    "start": "start_301",
                    "dead": "dead_301"
                },
                "Operational Improvement Task 302": {
                    "start": "start_302",
                    "dead": "dead_302"
                },
                "Operational Improvement Task 303": {
                    "start": "start_303",
                    "dead": "dead_303"
                },
                "Operational Improvement Task 304": {
                    "start": "start_304",
                    "dead": "dead_304"
                },
                "Operational Improvement Task 305": {
                    "start": "start_305",
                    "dead": "dead_305"
                },
                "Operational Improvement Task 306": {
                    "start": "start_306",
                    "dead": "dead_306"
                },
                "Operational Improvement Task 307": {
                    "start": "start_307",
                    "dead": "dead_307"
                },
                "Operational Improvement Task 308": {
                    "start": "start_308",
                    "dead": "dead_308"
                }
            },
            "Operational Improvements Batch 38": {
                "Operational Improvement Task 309": {
                    "start": "start_309",
                    "dead": "dead_309"
                },
                "Operational Improvement Task 310": {
                    "start": "start_310",
                    "dead": "dead_310"
                },
                "Operational Improvement Task 311": {
                    "start": "start_311",
                    "dead": "dead_311"
                },
                "Operational Improvement Task 312": {
                    "start": "start_312",
                    "dead": "dead_312"
                },
                "Operational Improvement Task 313": {
                    "start": "start_313",
                    "dead": "dead_313"
                },
                "Operational Improvement Task 314": {
                    "start": "start_314",
                    "dead": "dead_314"
                },
                "Operational Improvement Task 315": {
                    "start": "start_315",
                    "dead": "dead_315"
                },
                "Operational Improvement Task 316": {
                    "start": "start_316",
                    "dead": "dead_316"
                }
            },
            "Operational Improvements Batch 39": {
                "Operational Improvement Task 317": {
                    "start": "start_317",
                    "dead": "dead_317"
                },
                "Operational Improvement Task 318": {
                    "start": "start_318",
                    "dead": "dead_318"
                },
                "Operational Improvement Task 319": {
                    "start": "start_319",
                    "dead": "dead_319"
                }
            }
        }
    }
}
FE_PROJECTS = {
    "CVWritingSupporter Frontend": {
        "Build Infrastructure": {
            "Project Setup": {
                "Initialize Frontend Project Structure": {
                    "start": "start_1",
                    "dead": "dead_1"
                },
                "Configure Package Manager": {
                    "start": "start_2",
                    "dead": "dead_2"
                },
                "Set Up Linting Rules": {
                    "start": "start_3",
                    "dead": "dead_3"
                },
                "Configure Code Formatter": {
                    "start": "start_4",
                    "dead": "dead_4"
                },
                "Define Folder Architecture": {
                    "start": "start_5",
                    "dead": "dead_5"
                },
                "Configure Path Aliases": {
                    "start": "start_6",
                    "dead": "dead_6"
                },
                "Set Up Environment Variables": {
                    "start": "start_7",
                    "dead": "dead_7"
                },
                "Configure Build Scripts": {
                    "start": "start_8",
                    "dead": "dead_8"
                },
                "Initialize Git Hooks": {
                    "start": "start_9",
                    "dead": "dead_9"
                },
                "Set Up Commit Conventions": {
                    "start": "start_10",
                    "dead": "dead_10"
                },
                "Configure ESLint for React": {
                    "start": "start_11",
                    "dead": "dead_11"
                },
                "Configure Prettier Integration": {
                    "start": "start_12",
                    "dead": "dead_12"
                },
                "Set Up Base Stylesheet": {
                    "start": "start_13",
                    "dead": "dead_13"
                },
                "Configure Asset Management": {
                    "start": "start_14",
                    "dead": "dead_14"
                },
                "Initialize Localization Support": {
                    "start": "start_15",
                    "dead": "dead_15"
                },
                "Set Up Environment Switching": {
                    "start": "start_16",
                    "dead": "dead_16"
                },
                "Configure Development Server": {
                    "start": "start_17",
                    "dead": "dead_17"
                },
                "Verify Project Bootstrap": {
                    "start": "start_18",
                    "dead": "dead_18"
                },
                "Document Project Setup Steps": {
                    "start": "start_19",
                    "dead": "dead_19"
                },
                "Review Initial Setup": {
                    "start": "start_20",
                    "dead": "dead_20"
                },
                "Finalize Project Initialization": {
                    "start": "start_21",
                    "dead": "dead_21"
                }
            },
            "Build & Tooling": {
                "Configure Frontend Build Pipeline": {
                    "start": "start_22",
                    "dead": "dead_22"
                },
                "Optimize Build Output": {
                    "start": "start_23",
                    "dead": "dead_23"
                },
                "Set Up Hot Reloading": {
                    "start": "start_24",
                    "dead": "dead_24"
                },
                "Configure Source Maps": {
                    "start": "start_25",
                    "dead": "dead_25"
                },
                "Enable Tree Shaking": {
                    "start": "start_26",
                    "dead": "dead_26"
                },
                "Configure Environment-Based Builds": {
                    "start": "start_27",
                    "dead": "dead_27"
                },
                "Set Up Build Cache": {
                    "start": "start_28",
                    "dead": "dead_28"
                },
                "Analyze Bundle Size": {
                    "start": "start_29",
                    "dead": "dead_29"
                },
                "Split Vendor Bundles": {
                    "start": "start_30",
                    "dead": "dead_30"
                },
                "Optimize CSS Bundling": {
                    "start": "start_31",
                    "dead": "dead_31"
                },
                "Enable Lazy Loading": {
                    "start": "start_32",
                    "dead": "dead_32"
                },
                "Configure Asset Compression": {
                    "start": "start_33",
                    "dead": "dead_33"
                },
                "Validate Build Artifacts": {
                    "start": "start_34",
                    "dead": "dead_34"
                },
                "Handle Build Errors Gracefully": {
                    "start": "start_35",
                    "dead": "dead_35"
                },
                "Improve Build Performance": {
                    "start": "start_36",
                    "dead": "dead_36"
                },
                "Configure Build Logs": {
                    "start": "start_37",
                    "dead": "dead_37"
                },
                "Set Up Production Build": {
                    "start": "start_38",
                    "dead": "dead_38"
                },
                "Test Cross-Environment Builds": {
                    "start": "start_39",
                    "dead": "dead_39"
                },
                "Document Build Process": {
                    "start": "start_40",
                    "dead": "dead_40"
                },
                "Review Build Configuration": {
                    "start": "start_41",
                    "dead": "dead_41"
                }
            },
            "CI/CD Integration": {
                "Integrate Frontend CI Pipeline": {
                    "start": "start_42",
                    "dead": "dead_42"
                },
                "Configure Automated Builds": {
                    "start": "start_43",
                    "dead": "dead_43"
                },
                "Set Up Frontend Unit Test Stage": {
                    "start": "start_44",
                    "dead": "dead_44"
                },
                "Configure Lint Check Stage": {
                    "start": "start_45",
                    "dead": "dead_45"
                },
                "Enable Pull Request Validation": {
                    "start": "start_46",
                    "dead": "dead_46"
                },
                "Configure Artifact Publishing": {
                    "start": "start_47",
                    "dead": "dead_47"
                },
                "Set Up Deployment Trigger": {
                    "start": "start_48",
                    "dead": "dead_48"
                },
                "Integrate Environment Secrets": {
                    "start": "start_49",
                    "dead": "dead_49"
                },
                "Configure Rollback Mechanism": {
                    "start": "start_50",
                    "dead": "dead_50"
                },
                "Add Build Status Notifications": {
                    "start": "start_51",
                    "dead": "dead_51"
                },
                "Validate CI Pipeline Stability": {
                    "start": "start_52",
                    "dead": "dead_52"
                },
                "Optimize CI Execution Time": {
                    "start": "start_53",
                    "dead": "dead_53"
                },
                "Test CI Failure Scenarios": {
                    "start": "start_54",
                    "dead": "dead_54"
                },
                "Enable Manual Deployment Step": {
                    "start": "start_55",
                    "dead": "dead_55"
                },
                "Document CI/CD Workflow": {
                    "start": "start_56",
                    "dead": "dead_56"
                },
                "Review CI Security Settings": {
                    "start": "start_57",
                    "dead": "dead_57"
                },
                "Configure Multi-Branch Pipelines": {
                    "start": "start_58",
                    "dead": "dead_58"
                },
                "Validate Deployment Automation": {
                    "start": "start_59",
                    "dead": "dead_59"
                },
                "Improve CI Observability": {
                    "start": "start_60",
                    "dead": "dead_60"
                },
                "Finalize CI/CD Setup": {
                    "start": "start_61",
                    "dead": "dead_61"
                }
            },
            "Runtime Configuration": {
                "Configure Frontend Environment Variables": {
                    "start": "start_62",
                    "dead": "dead_62"
                },
                "Set Up API Endpoint Configuration": {
                    "start": "start_63",
                    "dead": "dead_63"
                },
                "Implement Runtime Config Loader": {
                    "start": "start_64",
                    "dead": "dead_64"
                },
                "Handle Environment Switching Logic": {
                    "start": "start_65",
                    "dead": "dead_65"
                },
                "Secure Runtime Secrets": {
                    "start": "start_66",
                    "dead": "dead_66"
                },
                "Validate Config at Startup": {
                    "start": "start_67",
                    "dead": "dead_67"
                },
                "Implement Feature Flag Support": {
                    "start": "start_68",
                    "dead": "dead_68"
                },
                "Configure CDN Endpoints": {
                    "start": "start_69",
                    "dead": "dead_69"
                },
                "Support Multi-Region Config": {
                    "start": "start_70",
                    "dead": "dead_70"
                },
                "Implement Config Caching": {
                    "start": "start_71",
                    "dead": "dead_71"
                },
                "Handle Missing Config Gracefully": {
                    "start": "start_72",
                    "dead": "dead_72"
                },
                "Document Runtime Configuration": {
                    "start": "start_73",
                    "dead": "dead_73"
                },
                "Review Config Security": {
                    "start": "start_74",
                    "dead": "dead_74"
                },
                "Test Runtime Config Overrides": {
                    "start": "start_75",
                    "dead": "dead_75"
                },
                "Optimize Config Loading": {
                    "start": "start_76",
                    "dead": "dead_76"
                },
                "Validate Production Config": {
                    "start": "start_77",
                    "dead": "dead_77"
                },
                "Audit Runtime Settings": {
                    "start": "start_78",
                    "dead": "dead_78"
                },
                "Refine Feature Flags": {
                    "start": "start_79",
                    "dead": "dead_79"
                },
                "Stabilize Runtime Behavior": {
                    "start": "start_80",
                    "dead": "dead_80"
                },
                "Finalize Runtime Configuration": {
                    "start": "start_81",
                    "dead": "dead_81"
                }
            },
            "Monitoring & Diagnostics": {
                "Integrate Frontend Error Tracking": {
                    "start": "start_82",
                    "dead": "dead_82"
                },
                "Set Up Performance Monitoring": {
                    "start": "start_83",
                    "dead": "dead_83"
                },
                "Track Frontend Load Time": {
                    "start": "start_84",
                    "dead": "dead_84"
                },
                "Configure Client-Side Logging": {
                    "start": "start_85",
                    "dead": "dead_85"
                },
                "Monitor API Call Failures": {
                    "start": "start_86",
                    "dead": "dead_86"
                },
                "Analyze User Interaction Metrics": {
                    "start": "start_87",
                    "dead": "dead_87"
                },
                "Detect Runtime Errors": {
                    "start": "start_88",
                    "dead": "dead_88"
                },
                "Configure Alert Thresholds": {
                    "start": "start_89",
                    "dead": "dead_89"
                },
                "Validate Monitoring Accuracy": {
                    "start": "start_90",
                    "dead": "dead_90"
                },
                "Optimize Logging Volume": {
                    "start": "start_91",
                    "dead": "dead_91"
                },
                "Enable Session Tracking": {
                    "start": "start_92",
                    "dead": "dead_92"
                },
                "Review Monitoring Dashboards": {
                    "start": "start_93",
                    "dead": "dead_93"
                },
                "Test Error Reporting Flow": {
                    "start": "start_94",
                    "dead": "dead_94"
                },
                "Improve Diagnostics Coverage": {
                    "start": "start_95",
                    "dead": "dead_95"
                },
                "Audit Monitoring Security": {
                    "start": "start_96",
                    "dead": "dead_96"
                },
                "Document Monitoring Setup": {
                    "start": "start_97",
                    "dead": "dead_97"
                },
                "Validate Production Monitoring": {
                    "start": "start_98",
                    "dead": "dead_98"
                },
                "Tune Performance Alerts": {
                    "start": "start_99",
                    "dead": "dead_99"
                },
                "Stabilize Monitoring System": {
                    "start": "start_100",
                    "dead": "dead_100"
                },
                "Finalize Monitoring & Diagnostics": {
                    "start": "start_101",
                    "dead": "dead_101"
                }
            }
        },
        "Main Frontend Services": {
            "Core UI Architecture": {
                "Design Core UI Architecture": {
                    "start": "start_102",
                    "dead": "dead_102"
                },
                "Define Component Hierarchy": {
                    "start": "start_103",
                    "dead": "dead_103"
                },
                "Establish UI Design Principles": {
                    "start": "start_104",
                    "dead": "dead_104"
                },
                "Create Shared Layout Components": {
                    "start": "start_105",
                    "dead": "dead_105"
                },
                "Implement Base Page Template": {
                    "start": "start_106",
                    "dead": "dead_106"
                },
                "Set Up Global Styling Strategy": {
                    "start": "start_107",
                    "dead": "dead_107"
                },
                "Configure Responsive Layout System": {
                    "start": "start_108",
                    "dead": "dead_108"
                },
                "Implement Reusable UI Utilities": {
                    "start": "start_109",
                    "dead": "dead_109"
                },
                "Build Common UI Components": {
                    "start": "start_110",
                    "dead": "dead_110"
                },
                "Standardize Component Props": {
                    "start": "start_111",
                    "dead": "dead_111"
                },
                "Define Component Naming Convention": {
                    "start": "start_112",
                    "dead": "dead_112"
                },
                "Create UI Component Documentation": {
                    "start": "start_113",
                    "dead": "dead_113"
                },
                "Integrate Design Tokens": {
                    "start": "start_114",
                    "dead": "dead_114"
                },
                "Implement Accessibility Base Rules": {
                    "start": "start_115",
                    "dead": "dead_115"
                },
                "Review UI Architecture Consistency": {
                    "start": "start_116",
                    "dead": "dead_116"
                },
                "Refine Component Composition": {
                    "start": "start_117",
                    "dead": "dead_117"
                },
                "Optimize UI Rendering Structure": {
                    "start": "start_118",
                    "dead": "dead_118"
                },
                "Validate UI Scalability": {
                    "start": "start_119",
                    "dead": "dead_119"
                },
                "Fix Architecture Edge Cases": {
                    "start": "start_120",
                    "dead": "dead_120"
                },
                "Finalize Core UI Architecture": {
                    "start": "start_121",
                    "dead": "dead_121"
                },
                "Sign Off UI Architecture": {
                    "start": "start_122",
                    "dead": "dead_122"
                }
            },
            "State Management": {
                "Design Global State Model": {
                    "start": "start_123",
                    "dead": "dead_123"
                },
                "Select State Management Approach": {
                    "start": "start_124",
                    "dead": "dead_124"
                },
                "Initialize State Store": {
                    "start": "start_125",
                    "dead": "dead_125"
                },
                "Implement Authentication State": {
                    "start": "start_126",
                    "dead": "dead_126"
                },
                "Implement User Profile State": {
                    "start": "start_127",
                    "dead": "dead_127"
                },
                "Handle Async State Transitions": {
                    "start": "start_128",
                    "dead": "dead_128"
                },
                "Implement Error State Handling": {
                    "start": "start_129",
                    "dead": "dead_129"
                },
                "Normalize API Response State": {
                    "start": "start_130",
                    "dead": "dead_130"
                },
                "Implement Loading Indicators State": {
                    "start": "start_131",
                    "dead": "dead_131"
                },
                "Optimize State Updates": {
                    "start": "start_132",
                    "dead": "dead_132"
                },
                "Prevent Redundant Re-renders": {
                    "start": "start_133",
                    "dead": "dead_133"
                },
                "Implement State Persistence": {
                    "start": "start_134",
                    "dead": "dead_134"
                },
                "Handle Logout State Cleanup": {
                    "start": "start_135",
                    "dead": "dead_135"
                },
                "Test State Consistency": {
                    "start": "start_136",
                    "dead": "dead_136"
                },
                "Fix State Race Conditions": {
                    "start": "start_137",
                    "dead": "dead_137"
                },
                "Refactor State Logic": {
                    "start": "start_138",
                    "dead": "dead_138"
                },
                "Document State Flow": {
                    "start": "start_139",
                    "dead": "dead_139"
                },
                "Review State Performance": {
                    "start": "start_140",
                    "dead": "dead_140"
                },
                "Stabilize State Management": {
                    "start": "start_141",
                    "dead": "dead_141"
                },
                "Finalize State Architecture": {
                    "start": "start_142",
                    "dead": "dead_142"
                }
            },
            "API Integration": {
                "Design API Integration Layer": {
                    "start": "start_143",
                    "dead": "dead_143"
                },
                "Implement API Client Wrapper": {
                    "start": "start_144",
                    "dead": "dead_144"
                },
                "Configure Authentication Headers": {
                    "start": "start_145",
                    "dead": "dead_145"
                },
                "Implement Request Interceptors": {
                    "start": "start_146",
                    "dead": "dead_146"
                },
                "Implement Response Interceptors": {
                    "start": "start_147",
                    "dead": "dead_147"
                },
                "Handle API Error Mapping": {
                    "start": "start_148",
                    "dead": "dead_148"
                },
                "Implement Retry Logic": {
                    "start": "start_149",
                    "dead": "dead_149"
                },
                "Support Pagination Handling": {
                    "start": "start_150",
                    "dead": "dead_150"
                },
                "Implement Search API Calls": {
                    "start": "start_151",
                    "dead": "dead_151"
                },
                "Integrate CV Analysis APIs": {
                    "start": "start_152",
                    "dead": "dead_152"
                },
                "Integrate CV Suggestion APIs": {
                    "start": "start_153",
                    "dead": "dead_153"
                },
                "Optimize API Call Frequency": {
                    "start": "start_154",
                    "dead": "dead_154"
                },
                "Implement Request Cancellation": {
                    "start": "start_155",
                    "dead": "dead_155"
                },
                "Secure Sensitive API Data": {
                    "start": "start_156",
                    "dead": "dead_156"
                },
                "Test API Integration Flows": {
                    "start": "start_157",
                    "dead": "dead_157"
                },
                "Fix API Edge Cases": {
                    "start": "start_158",
                    "dead": "dead_158"
                },
                "Refactor API Integration Layer": {
                    "start": "start_159",
                    "dead": "dead_159"
                },
                "Document API Usage": {
                    "start": "start_160",
                    "dead": "dead_160"
                },
                "Validate API Stability": {
                    "start": "start_161",
                    "dead": "dead_161"
                },
                "Finalize API Integration": {
                    "start": "start_162",
                    "dead": "dead_162"
                }
            },
            "Business Logic Components": {
                "Design Business Logic Separation": {
                    "start": "start_163",
                    "dead": "dead_163"
                },
                "Implement CV Parsing Logic": {
                    "start": "start_164",
                    "dead": "dead_164"
                },
                "Implement CV Scoring Logic": {
                    "start": "start_165",
                    "dead": "dead_165"
                },
                "Implement CV Recommendation Logic": {
                    "start": "start_166",
                    "dead": "dead_166"
                },
                "Handle Validation Rules": {
                    "start": "start_167",
                    "dead": "dead_167"
                },
                "Implement Form Submission Logic": {
                    "start": "start_168",
                    "dead": "dead_168"
                },
                "Handle Business Error Scenarios": {
                    "start": "start_169",
                    "dead": "dead_169"
                },
                "Implement Draft Saving Logic": {
                    "start": "start_170",
                    "dead": "dead_170"
                },
                "Handle Versioned CV Data": {
                    "start": "start_171",
                    "dead": "dead_171"
                },
                "Optimize Business Logic Execution": {
                    "start": "start_172",
                    "dead": "dead_172"
                },
                "Prevent Duplicate Submissions": {
                    "start": "start_173",
                    "dead": "dead_173"
                },
                "Implement Rule-Based Decisions": {
                    "start": "start_174",
                    "dead": "dead_174"
                },
                "Refactor Complex Logic Blocks": {
                    "start": "start_175",
                    "dead": "dead_175"
                },
                "Test Business Logic Accuracy": {
                    "start": "start_176",
                    "dead": "dead_176"
                },
                "Fix Logic Inconsistencies": {
                    "start": "start_177",
                    "dead": "dead_177"
                },
                "Document Business Logic": {
                    "start": "start_178",
                    "dead": "dead_178"
                },
                "Align Logic with Backend Rules": {
                    "start": "start_179",
                    "dead": "dead_179"
                },
                "Review Business Logic Performance": {
                    "start": "start_180",
                    "dead": "dead_180"
                },
                "Stabilize Business Logic": {
                    "start": "start_181",
                    "dead": "dead_181"
                },
                "Finalize Business Logic Layer": {
                    "start": "start_182",
                    "dead": "dead_182"
                }
            },
            "Performance & UX Optimization": {
                "Analyze Frontend Performance Bottlenecks": {
                    "start": "start_183",
                    "dead": "dead_183"
                },
                "Optimize Initial Page Load": {
                    "start": "start_184",
                    "dead": "dead_184"
                },
                "Reduce Unnecessary Re-renders": {
                    "start": "start_185",
                    "dead": "dead_185"
                },
                "Optimize Component Memoization": {
                    "start": "start_186",
                    "dead": "dead_186"
                },
                "Improve API Response Handling UX": {
                    "start": "start_187",
                    "dead": "dead_187"
                },
                "Optimize Form Interaction UX": {
                    "start": "start_188",
                    "dead": "dead_188"
                },
                "Improve Error Feedback UX": {
                    "start": "start_189",
                    "dead": "dead_189"
                },
                "Optimize Mobile Responsiveness": {
                    "start": "start_190",
                    "dead": "dead_190"
                },
                "Implement Skeleton Loading": {
                    "start": "start_191",
                    "dead": "dead_191"
                },
                "Optimize Animation Performance": {
                    "start": "start_192",
                    "dead": "dead_192"
                },
                "Reduce Frontend Memory Usage": {
                    "start": "start_193",
                    "dead": "dead_193"
                },
                "Improve Accessibility UX": {
                    "start": "start_194",
                    "dead": "dead_194"
                },
                "Optimize Large List Rendering": {
                    "start": "start_195",
                    "dead": "dead_195"
                },
                "Test UX Under Load": {
                    "start": "start_196",
                    "dead": "dead_196"
                },
                "Fix UX Regression Issues": {
                    "start": "start_197",
                    "dead": "dead_197"
                },
                "Refine User Interaction Flow": {
                    "start": "start_198",
                    "dead": "dead_198"
                },
                "Document UX Improvements": {
                    "start": "start_199",
                    "dead": "dead_199"
                },
                "Validate Performance Gains": {
                    "start": "start_200",
                    "dead": "dead_200"
                },
                "Stabilize UX Performance": {
                    "start": "start_201",
                    "dead": "dead_201"
                },
                "Finalize Frontend Services": {
                    "start": "start_202",
                    "dead": "dead_202"
                }
            }
        },
        "Refactor Frontend Services": {
            "Codebase Refactoring": {
                "Refactor Component Folder Structure": {
                    "start": "start_203",
                    "dead": "dead_203"
                },
                "Remove Unused UI Components": {
                    "start": "start_204",
                    "dead": "dead_204"
                },
                "Standardize Component Naming": {
                    "start": "start_205",
                    "dead": "dead_205"
                },
                "Refactor Shared UI Utilities": {
                    "start": "start_206",
                    "dead": "dead_206"
                },
                "Simplify Complex Component Logic": {
                    "start": "start_207",
                    "dead": "dead_207"
                },
                "Refactor Custom Hooks": {
                    "start": "start_208",
                    "dead": "dead_208"
                },
                "Improve Component Reusability": {
                    "start": "start_209",
                    "dead": "dead_209"
                },
                "Decouple UI and Business Logic": {
                    "start": "start_210",
                    "dead": "dead_210"
                },
                "Refactor Form Handling Components": {
                    "start": "start_211",
                    "dead": "dead_211"
                },
                "Refactor Modal and Dialog Logic": {
                    "start": "start_212",
                    "dead": "dead_212"
                },
                "Cleanup Deprecated UI Patterns": {
                    "start": "start_213",
                    "dead": "dead_213"
                },
                "Refactor Layout Components": {
                    "start": "start_214",
                    "dead": "dead_214"
                },
                "Improve Code Readability": {
                    "start": "start_215",
                    "dead": "dead_215"
                },
                "Apply Consistent Styling Rules": {
                    "start": "start_216",
                    "dead": "dead_216"
                },
                "Reduce Component Coupling": {
                    "start": "start_217",
                    "dead": "dead_217"
                },
                "Refactor Conditional Rendering Logic": {
                    "start": "start_218",
                    "dead": "dead_218"
                },
                "Remove Dead Code Paths": {
                    "start": "start_219",
                    "dead": "dead_219"
                },
                "Align Refactored Code with Standards": {
                    "start": "start_220",
                    "dead": "dead_220"
                },
                "Verify Refactored Components": {
                    "start": "start_221",
                    "dead": "dead_221"
                },
                "Fix Refactor Regression Issues": {
                    "start": "start_222",
                    "dead": "dead_222"
                },
                "Finalize UI Codebase Refactor": {
                    "start": "start_223",
                    "dead": "dead_223"
                }
            },
            "Performance Optimization": {
                "Profile Frontend Performance Hotspots": {
                    "start": "start_224",
                    "dead": "dead_224"
                },
                "Optimize Component Re-rendering": {
                    "start": "start_225",
                    "dead": "dead_225"
                },
                "Memoize Expensive Computations": {
                    "start": "start_226",
                    "dead": "dead_226"
                },
                "Reduce Bundle Size": {
                    "start": "start_227",
                    "dead": "dead_227"
                },
                "Optimize Code Splitting Strategy": {
                    "start": "start_228",
                    "dead": "dead_228"
                },
                "Lazy Load Heavy UI Modules": {
                    "start": "start_229",
                    "dead": "dead_229"
                },
                "Optimize Image Loading": {
                    "start": "start_230",
                    "dead": "dead_230"
                },
                "Reduce Runtime Memory Usage": {
                    "start": "start_231",
                    "dead": "dead_231"
                },
                "Optimize Virtual DOM Updates": {
                    "start": "start_232",
                    "dead": "dead_232"
                },
                "Improve Initial Render Time": {
                    "start": "start_233",
                    "dead": "dead_233"
                },
                "Optimize Event Handling Logic": {
                    "start": "start_234",
                    "dead": "dead_234"
                },
                "Reduce Unnecessary Network Requests": {
                    "start": "start_235",
                    "dead": "dead_235"
                },
                "Optimize Animation Performance": {
                    "start": "start_236",
                    "dead": "dead_236"
                },
                "Optimize Large List Rendering": {
                    "start": "start_237",
                    "dead": "dead_237"
                },
                "Benchmark Performance Improvements": {
                    "start": "start_238",
                    "dead": "dead_238"
                },
                "Fix Performance Regression Issues": {
                    "start": "start_239",
                    "dead": "dead_239"
                },
                "Stabilize Performance Enhancements": {
                    "start": "start_240",
                    "dead": "dead_240"
                },
                "Document Performance Changes": {
                    "start": "start_241",
                    "dead": "dead_241"
                },
                "Validate Performance Gains": {
                    "start": "start_242",
                    "dead": "dead_242"
                },
                "Finalize Performance Optimization": {
                    "start": "start_243",
                    "dead": "dead_243"
                }
            },
            "Bug Fixing & Stability": {
                "Analyze Frontend Bug Reports": {
                    "start": "start_244",
                    "dead": "dead_244"
                },
                "Fix UI Rendering Issues": {
                    "start": "start_245",
                    "dead": "dead_245"
                },
                "Resolve State Synchronization Bugs": {
                    "start": "start_246",
                    "dead": "dead_246"
                },
                "Fix API Integration Edge Cases": {
                    "start": "start_247",
                    "dead": "dead_247"
                },
                "Resolve Race Condition Issues": {
                    "start": "start_248",
                    "dead": "dead_248"
                },
                "Fix Form Validation Bugs": {
                    "start": "start_249",
                    "dead": "dead_249"
                },
                "Fix Authentication Flow Issues": {
                    "start": "start_250",
                    "dead": "dead_250"
                },
                "Fix Permission Handling Bugs": {
                    "start": "start_251",
                    "dead": "dead_251"
                },
                "Fix Responsive Layout Issues": {
                    "start": "start_252",
                    "dead": "dead_252"
                },
                "Resolve Browser Compatibility Issues": {
                    "start": "start_253",
                    "dead": "dead_253"
                },
                "Fix Accessibility Defects": {
                    "start": "start_254",
                    "dead": "dead_254"
                },
                "Resolve Memory Leak Issues": {
                    "start": "start_255",
                    "dead": "dead_255"
                },
                "Fix Error Handling Gaps": {
                    "start": "start_256",
                    "dead": "dead_256"
                },
                "Fix Navigation Flow Bugs": {
                    "start": "start_257",
                    "dead": "dead_257"
                },
                "Fix UI Regression Issues": {
                    "start": "start_258",
                    "dead": "dead_258"
                },
                "Stabilize UI Behavior": {
                    "start": "start_259",
                    "dead": "dead_259"
                },
                "Verify Bug Fixes": {
                    "start": "start_260",
                    "dead": "dead_260"
                },
                "Re-test Fixed Scenarios": {
                    "start": "start_261",
                    "dead": "dead_261"
                },
                "Close Outstanding UI Issues": {
                    "start": "start_262",
                    "dead": "dead_262"
                },
                "Finalize Stability Fixes": {
                    "start": "start_263",
                    "dead": "dead_263"
                }
            },
            "UX & Accessibility Improvements": {
                "Review User Feedback Reports": {
                    "start": "start_264",
                    "dead": "dead_264"
                },
                "Improve Form Usability": {
                    "start": "start_265",
                    "dead": "dead_265"
                },
                "Improve Error Message Clarity": {
                    "start": "start_266",
                    "dead": "dead_266"
                },
                "Enhance Keyboard Navigation": {
                    "start": "start_267",
                    "dead": "dead_267"
                },
                "Improve Screen Reader Support": {
                    "start": "start_268",
                    "dead": "dead_268"
                },
                "Enhance Visual Accessibility": {
                    "start": "start_269",
                    "dead": "dead_269"
                },
                "Improve Mobile Interaction UX": {
                    "start": "start_270",
                    "dead": "dead_270"
                },
                "Optimize Page Flow UX": {
                    "start": "start_271",
                    "dead": "dead_271"
                },
                "Improve Loading Feedback UX": {
                    "start": "start_272",
                    "dead": "dead_272"
                },
                "Improve Empty State UX": {
                    "start": "start_273",
                    "dead": "dead_273"
                },
                "Improve Error Recovery UX": {
                    "start": "start_274",
                    "dead": "dead_274"
                },
                "Refine UI Micro-interactions": {
                    "start": "start_275",
                    "dead": "dead_275"
                },
                "Improve CV Editing Experience": {
                    "start": "start_276",
                    "dead": "dead_276"
                },
                "Improve Content Readability": {
                    "start": "start_277",
                    "dead": "dead_277"
                },
                "Fix UX Inconsistencies": {
                    "start": "start_278",
                    "dead": "dead_278"
                },
                "Validate Accessibility Compliance": {
                    "start": "start_279",
                    "dead": "dead_279"
                },
                "Test UX Improvements": {
                    "start": "start_280",
                    "dead": "dead_280"
                },
                "Collect UX Validation Feedback": {
                    "start": "start_281",
                    "dead": "dead_281"
                },
                "Finalize UX Improvements": {
                    "start": "start_282",
                    "dead": "dead_282"
                },
                "Sign Off UX Enhancements": {
                    "start": "start_283",
                    "dead": "dead_283"
                }
            },
            "Cleanup & Documentation": {
                "Remove Deprecated Frontend Features": {
                    "start": "start_284",
                    "dead": "dead_284"
                },
                "Cleanup Feature Flags": {
                    "start": "start_285",
                    "dead": "dead_285"
                },
                "Update Frontend Documentation": {
                    "start": "start_286",
                    "dead": "dead_286"
                },
                "Update Component Usage Guides": {
                    "start": "start_287",
                    "dead": "dead_287"
                },
                "Document Refactored Architecture": {
                    "start": "start_288",
                    "dead": "dead_288"
                },
                "Document Performance Improvements": {
                    "start": "start_289",
                    "dead": "dead_289"
                },
                "Document Known Limitations": {
                    "start": "start_290",
                    "dead": "dead_290"
                },
                "Review Documentation Accuracy": {
                    "start": "start_291",
                    "dead": "dead_291"
                },
                "Align Docs with Backend Changes": {
                    "start": "start_292",
                    "dead": "dead_292"
                },
                "Prepare Release Notes": {
                    "start": "start_293",
                    "dead": "dead_293"
                },
                "Conduct Final Frontend Review": {
                    "start": "start_294",
                    "dead": "dead_294"
                },
                "Address Review Feedback": {
                    "start": "start_295",
                    "dead": "dead_295"
                },
                "Finalize Frontend Cleanup": {
                    "start": "start_296",
                    "dead": "dead_296"
                },
                "Stabilize Release Candidate": {
                    "start": "start_297",
                    "dead": "dead_297"
                },
                "Validate Final Build": {
                    "start": "start_298",
                    "dead": "dead_298"
                },
                "Prepare Production Deployment": {
                    "start": "start_299",
                    "dead": "dead_299"
                },
                "Sign Off Frontend Release": {
                    "start": "start_300",
                    "dead": "dead_300"
                },
                "Post-Release Verification": {
                    "start": "start_301",
                    "dead": "dead_301"
                },
                "Close Frontend Refactor Phase": {
                    "start": "start_302",
                    "dead": "dead_302"
                },
                "Archive Refactor Artifacts": {
                    "start": "start_303",
                    "dead": "dead_303"
                }
            }
        }
    }
}
BA_PROJECTS = {
    "CVWritingSupporter BusinessAnalysis": {
        "Database Design": {
            "Business Requirements Analysis": {
                "Analyze CV Data Requirements": {
                    "start": "start_1",
                    "dead": "dead_1"
                },
                "Identify Core CV Entities": {
                    "start": "start_2",
                    "dead": "dead_2"
                },
                "Define User Data Scope": {
                    "start": "start_3",
                    "dead": "dead_3"
                },
                "Analyze CV Versioning Needs": {
                    "start": "start_4",
                    "dead": "dead_4"
                },
                "Identify Data Ownership Rules": {
                    "start": "start_5",
                    "dead": "dead_5"
                },
                "Analyze CV Template Data": {
                    "start": "start_6",
                    "dead": "dead_6"
                },
                "Define CV History Tracking Rules": {
                    "start": "start_7",
                    "dead": "dead_7"
                },
                "Identify Required Metadata Fields": {
                    "start": "start_8",
                    "dead": "dead_8"
                },
                "Analyze Search & Filter Requirements": {
                    "start": "start_9",
                    "dead": "dead_9"
                },
                "Define Audit Data Needs": {
                    "start": "start_10",
                    "dead": "dead_10"
                },
                "Identify Reporting Data Needs": {
                    "start": "start_11",
                    "dead": "dead_11"
                },
                "Analyze Data Retention Rules": {
                    "start": "start_12",
                    "dead": "dead_12"
                },
                "Define GDPR-related Data Constraints": {
                    "start": "start_13",
                    "dead": "dead_13"
                },
                "Analyze Data Access Permissions": {
                    "start": "start_14",
                    "dead": "dead_14"
                },
                "Identify Integration Data Needs": {
                    "start": "start_15",
                    "dead": "dead_15"
                },
                "Validate Data Completeness Rules": {
                    "start": "start_16",
                    "dead": "dead_16"
                },
                "Analyze Error Logging Data": {
                    "start": "start_17",
                    "dead": "dead_17"
                },
                "Define Business Data Glossary": {
                    "start": "start_18",
                    "dead": "dead_18"
                },
                "Review Business Data Assumptions": {
                    "start": "start_19",
                    "dead": "dead_19"
                },
                "Sign Off Business Data Requirements": {
                    "start": "start_20",
                    "dead": "dead_20"
                }
            },
            "Logical Data Modeling": {
                "Define Logical CV Data Model": {
                    "start": "start_21",
                    "dead": "dead_21"
                },
                "Map Entities to Business Concepts": {
                    "start": "start_22",
                    "dead": "dead_22"
                },
                "Define Entity Relationships": {
                    "start": "start_23",
                    "dead": "dead_23"
                },
                "Analyze Normalization Level": {
                    "start": "start_24",
                    "dead": "dead_24"
                },
                "Define CV–User Relationship": {
                    "start": "start_25",
                    "dead": "dead_25"
                },
                "Define CV–Template Mapping": {
                    "start": "start_26",
                    "dead": "dead_26"
                },
                "Model Versioned CV Structure": {
                    "start": "start_27",
                    "dead": "dead_27"
                },
                "Define Audit Trail Structure": {
                    "start": "start_28",
                    "dead": "dead_28"
                },
                "Model Recommendation Data Flow": {
                    "start": "start_29",
                    "dead": "dead_29"
                },
                "Define Status Lifecycle Fields": {
                    "start": "start_30",
                    "dead": "dead_30"
                },
                "Validate Cardinality Rules": {
                    "start": "start_31",
                    "dead": "dead_31"
                },
                "Resolve Data Ambiguities": {
                    "start": "start_32",
                    "dead": "dead_32"
                },
                "Align Model with Business Rules": {
                    "start": "start_33",
                    "dead": "dead_33"
                },
                "Validate Logical Model Consistency": {
                    "start": "start_34",
                    "dead": "dead_34"
                },
                "Review Logical Constraints": {
                    "start": "start_35",
                    "dead": "dead_35"
                },
                "Optimize Logical Model Simplicity": {
                    "start": "start_36",
                    "dead": "dead_36"
                },
                "Document Logical Data Model": {
                    "start": "start_37",
                    "dead": "dead_37"
                },
                "Review with Backend Team": {
                    "start": "start_38",
                    "dead": "dead_38"
                },
                "Apply Feedback to Model": {
                    "start": "start_39",
                    "dead": "dead_39"
                },
                "Finalize Logical Data Model": {
                    "start": "start_40",
                    "dead": "dead_40"
                }
            },
            "Data Validation & Review": {
                "Define Business Validation Rules": {
                    "start": "start_41",
                    "dead": "dead_41"
                },
                "Define Mandatory Field Rules": {
                    "start": "start_42",
                    "dead": "dead_42"
                },
                "Define Cross-field Validation": {
                    "start": "start_43",
                    "dead": "dead_43"
                },
                "Analyze Data Quality Risks": {
                    "start": "start_44",
                    "dead": "dead_44"
                },
                "Define Duplicate Detection Rules": {
                    "start": "start_45",
                    "dead": "dead_45"
                },
                "Review Edge Case Scenarios": {
                    "start": "start_46",
                    "dead": "dead_46"
                },
                "Validate Error Handling Scenarios": {
                    "start": "start_47",
                    "dead": "dead_47"
                },
                "Align Validation with BE Logic": {
                    "start": "start_48",
                    "dead": "dead_48"
                },
                "Review Data Consistency Rules": {
                    "start": "start_49",
                    "dead": "dead_49"
                },
                "Analyze Impact of Invalid Data": {
                    "start": "start_50",
                    "dead": "dead_50"
                },
                "Define Data Correction Scenarios": {
                    "start": "start_51",
                    "dead": "dead_51"
                },
                "Validate Migration Data Rules": {
                    "start": "start_52",
                    "dead": "dead_52"
                },
                "Review Historical Data Handling": {
                    "start": "start_53",
                    "dead": "dead_53"
                },
                "Define Data Review Checklist": {
                    "start": "start_54",
                    "dead": "dead_54"
                },
                "Conduct Data Review Workshop": {
                    "start": "start_55",
                    "dead": "dead_55"
                },
                "Document Validation Findings": {
                    "start": "start_56",
                    "dead": "dead_56"
                },
                "Resolve Validation Conflicts": {
                    "start": "start_57",
                    "dead": "dead_57"
                },
                "Confirm Validation Coverage": {
                    "start": "start_58",
                    "dead": "dead_58"
                },
                "Get Stakeholder Approval": {
                    "start": "start_59",
                    "dead": "dead_59"
                },
                "Sign Off Database Design Phase": {
                    "start": "start_60",
                    "dead": "dead_60"
                }
            }
        },
        "Main Business Rules Analysis": {
            "Core Business Rules": {
                "Identify CV Creation Rules": {
                    "start": "start_61",
                    "dead": "dead_61"
                },
                "Define CV Editing Constraints": {
                    "start": "start_62",
                    "dead": "dead_62"
                },
                "Define CV Submission Rules": {
                    "start": "start_63",
                    "dead": "dead_63"
                },
                "Analyze CV Scoring Criteria": {
                    "start": "start_64",
                    "dead": "dead_64"
                },
                "Define Recommendation Triggers": {
                    "start": "start_65",
                    "dead": "dead_65"
                },
                "Identify User Role Permissions": {
                    "start": "start_66",
                    "dead": "dead_66"
                },
                "Define Visibility Rules": {
                    "start": "start_67",
                    "dead": "dead_67"
                },
                "Analyze Approval Workflows": {
                    "start": "start_68",
                    "dead": "dead_68"
                },
                "Define CV Status Transitions": {
                    "start": "start_69",
                    "dead": "dead_69"
                },
                "Define Error Handling Rules": {
                    "start": "start_70",
                    "dead": "dead_70"
                },
                "Define Notification Triggers": {
                    "start": "start_71",
                    "dead": "dead_71"
                },
                "Analyze Retry & Recovery Rules": {
                    "start": "start_72",
                    "dead": "dead_72"
                },
                "Define SLA-related Rules": {
                    "start": "start_73",
                    "dead": "dead_73"
                },
                "Align Rules with Backend Logic": {
                    "start": "start_74",
                    "dead": "dead_74"
                },
                "Resolve Rule Conflicts": {
                    "start": "start_75",
                    "dead": "dead_75"
                },
                "Validate Business Rule Coverage": {
                    "start": "start_76",
                    "dead": "dead_76"
                },
                "Document Business Rules": {
                    "start": "start_77",
                    "dead": "dead_77"
                },
                "Review Rules with Stakeholders": {
                    "start": "start_78",
                    "dead": "dead_78"
                },
                "Refine Business Rules": {
                    "start": "start_79",
                    "dead": "dead_79"
                },
                "Sign Off Core Business Rules": {
                    "start": "start_80",
                    "dead": "dead_80"
                }
            },
            "Process Flow Analysis": {
                "Define CV End-to-End Flow": {
                    "start": "start_81",
                    "dead": "dead_81"
                },
                "Map User Interaction Flow": {
                    "start": "start_82",
                    "dead": "dead_82"
                },
                "Define Exception Flows": {
                    "start": "start_83",
                    "dead": "dead_83"
                },
                "Analyze Failure Scenarios": {
                    "start": "start_84",
                    "dead": "dead_84"
                },
                "Define Recovery Processes": {
                    "start": "start_85",
                    "dead": "dead_85"
                },
                "Align Process with FE UX": {
                    "start": "start_86",
                    "dead": "dead_86"
                },
                "Align Process with BE Services": {
                    "start": "start_87",
                    "dead": "dead_87"
                },
                "Define Integration Touchpoints": {
                    "start": "start_88",
                    "dead": "dead_88"
                },
                "Identify Bottlenecks": {
                    "start": "start_89",
                    "dead": "dead_89"
                },
                "Optimize Process Efficiency": {
                    "start": "start_90",
                    "dead": "dead_90"
                },
                "Validate Parallel Flows": {
                    "start": "start_91",
                    "dead": "dead_91"
                },
                "Define Manual Intervention Points": {
                    "start": "start_92",
                    "dead": "dead_92"
                },
                "Document Process Flow Diagrams": {
                    "start": "start_93",
                    "dead": "dead_93"
                },
                "Review Flow with Team": {
                    "start": "start_94",
                    "dead": "dead_94"
                },
                "Apply Feedback to Flows": {
                    "start": "start_95",
                    "dead": "dead_95"
                },
                "Validate End-to-End Scenarios": {
                    "start": "start_96",
                    "dead": "dead_96"
                },
                "Resolve Flow Inconsistencies": {
                    "start": "start_97",
                    "dead": "dead_97"
                },
                "Finalize Process Flows": {
                    "start": "start_98",
                    "dead": "dead_98"
                },
                "Approve Process Definitions": {
                    "start": "start_99",
                    "dead": "dead_99"
                },
                "Sign Off BA Phase": {
                    "start": "start_100",
                    "dead": "dead_100"
                }
            },
            "Cross-Domain Alignment Rules": {
                "Align Business Rules with Backend Logic": {
                    "start": "start_101",
                    "dead": "dead_101"
                },
                "Align Business Rules with Frontend UX": {
                    "start": "start_102",
                    "dead": "dead_102"
                },
                "Validate API Contract Against Business Rules": {
                    "start": "start_103",
                    "dead": "dead_103"
                },
                "Review Data Flow Across Domains": {
                    "start": "start_104",
                    "dead": "dead_104"
                },
                "Identify Cross-Domain Rule Conflicts": {
                    "start": "start_105",
                    "dead": "dead_105"
                },
                "Resolve Backend–Frontend Rule Mismatches": {
                    "start": "start_106",
                    "dead": "dead_106"
                },
                "Validate End-to-End Business Scenarios": {
                    "start": "start_107",
                    "dead": "dead_107"
                },
                "Align Error Handling Between Domains": {
                    "start": "start_108",
                    "dead": "dead_108"
                },
                "Validate Permission Rules Across Services": {
                    "start": "start_109",
                    "dead": "dead_109"
                },
                "Review Authentication & Authorization Flows": {
                    "start": "start_110",
                    "dead": "dead_110"
                },
                "Align Validation Rules Across Layers": {
                    "start": "start_111",
                    "dead": "dead_111"
                },
                "Validate Business Logic Execution Order": {
                    "start": "start_112",
                    "dead": "dead_112"
                },
                "Analyze Impact of Async Processing on Business Rules": {
                    "start": "start_113",
                    "dead": "dead_113"
                },
                "Review Transaction Boundaries": {
                    "start": "start_114",
                    "dead": "dead_114"
                },
                "Validate Data Consistency Across Services": {
                    "start": "start_115",
                    "dead": "dead_115"
                },
                "Align Logging & Audit Requirements": {
                    "start": "start_116",
                    "dead": "dead_116"
                },
                "Validate Reporting Data Sources": {
                    "start": "start_117",
                    "dead": "dead_117"
                },
                "Confirm Business KPI Traceability": {
                    "start": "start_118",
                    "dead": "dead_118"
                },
                "Finalize Cross-Domain Alignment": {
                    "start": "start_119",
                    "dead": "dead_119"
                },
                "Sign Off Cross-Domain Business Rules": {
                    "start": "start_120",
                    "dead": "dead_120"
                }
            },
            "Exception & Edge Case Rules": {
                "Identify CV Incomplete Submission Rules": {
                    "start": "start_121",
                    "dead": "dead_121"
                },
                "Define Missing Field Handling Rules": {
                    "start": "start_122",
                    "dead": "dead_122"
                },
                "Analyze Invalid CV Format Scenarios": {
                    "start": "start_123",
                    "dead": "dead_123"
                },
                "Define Duplicate CV Detection Rules": {
                    "start": "start_124",
                    "dead": "dead_124"
                },
                "Analyze Concurrent Edit Scenarios": {
                    "start": "start_125",
                    "dead": "dead_125"
                },
                "Define Conflict Resolution Rules": {
                    "start": "start_126",
                    "dead": "dead_126"
                },
                "Identify API Failure Business Impact": {
                    "start": "start_127",
                    "dead": "dead_127"
                },
                "Define Timeout Handling Rules": {
                    "start": "start_128",
                    "dead": "dead_128"
                },
                "Analyze Partial Save Scenarios": {
                    "start": "start_129",
                    "dead": "dead_129"
                },
                "Define Rollback Business Rules": {
                    "start": "start_130",
                    "dead": "dead_130"
                },
                "Identify Unauthorized Access Scenarios": {
                    "start": "start_131",
                    "dead": "dead_131"
                },
                "Define Security Violation Handling": {
                    "start": "start_132",
                    "dead": "dead_132"
                },
                "Analyze Data Corruption Impact": {
                    "start": "start_133",
                    "dead": "dead_133"
                },
                "Define Recovery Business Rules": {
                    "start": "start_134",
                    "dead": "dead_134"
                },
                "Identify System Degradation Scenarios": {
                    "start": "start_135",
                    "dead": "dead_135"
                },
                "Define Graceful Degradation Rules": {
                    "start": "start_136",
                    "dead": "dead_136"
                },
                "Analyze Cross-Service Failure Impact": {
                    "start": "start_137",
                    "dead": "dead_137"
                },
                "Define Escalation Rules": {
                    "start": "start_138",
                    "dead": "dead_138"
                },
                "Validate Edge Case Coverage": {
                    "start": "start_139",
                    "dead": "dead_139"
                },
                "Sign Off Exception Handling Rules": {
                    "start": "start_140",
                    "dead": "dead_140"
                }
            },
            "Reporting & Analytics Rules": {
                "Identify Business Metrics Requirements": {
                    "start": "start_141",
                    "dead": "dead_141"
                },
                "Define CV Usage Metrics": {
                    "start": "start_142",
                    "dead": "dead_142"
                },
                "Define CV Quality Scoring Metrics": {
                    "start": "start_143",
                    "dead": "dead_143"
                },
                "Analyze Recommendation Effectiveness KPIs": {
                    "start": "start_144",
                    "dead": "dead_144"
                },
                "Define User Engagement Metrics": {
                    "start": "start_145",
                    "dead": "dead_145"
                },
                "Define Conversion Tracking Rules": {
                    "start": "start_146",
                    "dead": "dead_146"
                },
                "Analyze Funnel Drop-off Points": {
                    "start": "start_147",
                    "dead": "dead_147"
                },
                "Define Data Aggregation Rules": {
                    "start": "start_148",
                    "dead": "dead_148"
                },
                "Define Time-based Reporting Rules": {
                    "start": "start_149",
                    "dead": "dead_149"
                },
                "Define Role-based Report Visibility": {
                    "start": "start_150",
                    "dead": "dead_150"
                },
                "Analyze Data Accuracy Constraints": {
                    "start": "start_151",
                    "dead": "dead_151"
                },
                "Define Metric Validation Rules": {
                    "start": "start_152",
                    "dead": "dead_152"
                },
                "Align Reporting with Database Model": {
                    "start": "start_153",
                    "dead": "dead_153"
                },
                "Align Reporting with Backend APIs": {
                    "start": "start_154",
                    "dead": "dead_154"
                },
                "Define Historical Reporting Rules": {
                    "start": "start_155",
                    "dead": "dead_155"
                },
                "Define Export & Sharing Rules": {
                    "start": "start_156",
                    "dead": "dead_156"
                },
                "Validate Analytics Use Cases": {
                    "start": "start_157",
                    "dead": "dead_157"
                },
                "Review Metrics with Stakeholders": {
                    "start": "start_158",
                    "dead": "dead_158"
                },
                "Finalize Reporting Rules": {
                    "start": "start_159",
                    "dead": "dead_159"
                },
                "Sign Off Analytics Rules": {
                    "start": "start_160",
                    "dead": "dead_160"
                }
            }
        },
        "Client Requests #1": {
            "Requirement Changes & Clarification": {
                "Analyze Client Change Request Summary": {
                    "start": "start_161",
                    "dead": "dead_161"
                },
                "Clarify Updated CV Creation Requirements": {
                    "start": "start_162",
                    "dead": "dead_162"
                },
                "Analyze Changes in CV Editing Flow": {
                    "start": "start_163",
                    "dead": "dead_163"
                },
                "Clarify New CV Submission Constraints": {
                    "start": "start_164",
                    "dead": "dead_164"
                },
                "Analyze Updated Scoring Expectations": {
                    "start": "start_165",
                    "dead": "dead_165"
                },
                "Clarify Recommendation Logic Changes": {
                    "start": "start_166",
                    "dead": "dead_166"
                },
                "Identify Deprecated Business Rules": {
                    "start": "start_167",
                    "dead": "dead_167"
                },
                "Identify Newly Added Business Rules": {
                    "start": "start_168",
                    "dead": "dead_168"
                },
                "Analyze Impact on User Roles": {
                    "start": "start_169",
                    "dead": "dead_169"
                },
                "Clarify Permission Model Changes": {
                    "start": "start_170",
                    "dead": "dead_170"
                },
                "Analyze Change in Data Visibility Rules": {
                    "start": "start_171",
                    "dead": "dead_171"
                },
                "Clarify Audit & Logging Expectations": {
                    "start": "start_172",
                    "dead": "dead_172"
                },
                "Analyze Updated Error Handling Rules": {
                    "start": "start_173",
                    "dead": "dead_173"
                },
                "Clarify Edge Case Handling Updates": {
                    "start": "start_174",
                    "dead": "dead_174"
                },
                "Analyze New Validation Requirements": {
                    "start": "start_175",
                    "dead": "dead_175"
                },
                "Clarify Client Terminology Changes": {
                    "start": "start_176",
                    "dead": "dead_176"
                },
                "Resolve Ambiguous Client Statements": {
                    "start": "start_177",
                    "dead": "dead_177"
                },
                "Update Business Glossary": {
                    "start": "start_178",
                    "dead": "dead_178"
                },
                "Confirm Clarified Requirements with Client": {
                    "start": "start_179",
                    "dead": "dead_179"
                },
                "Sign Off Clarified Requirements": {
                    "start": "start_180",
                    "dead": "dead_180"
                },
                "Analyze Additional Client Feedback": {
                    "start": "start_181",
                    "dead": "dead_181"
                },
                "Clarify Priority Changes from Client": {
                    "start": "start_182",
                    "dead": "dead_182"
                },
                "Analyze Change Dependencies": {
                    "start": "start_183",
                    "dead": "dead_183"
                },
                "Identify Conflicting Change Requests": {
                    "start": "start_184",
                    "dead": "dead_184"
                },
                "Resolve Requirement Conflicts": {
                    "start": "start_185",
                    "dead": "dead_185"
                },
                "Re-validate Business Scope": {
                    "start": "start_186",
                    "dead": "dead_186"
                },
                "Confirm Non-functional Requirement Changes": {
                    "start": "start_187",
                    "dead": "dead_187"
                }
            },
            "Impact Analysis & Re-alignment": {
                "Analyze Impact on Backend Services": {
                    "start": "start_188",
                    "dead": "dead_188"
                },
                "Analyze Impact on Frontend UX": {
                    "start": "start_189",
                    "dead": "dead_189"
                },
                "Analyze Impact on Database Schema": {
                    "start": "start_190",
                    "dead": "dead_190"
                },
                "Analyze Impact on API Contracts": {
                    "start": "start_191",
                    "dead": "dead_191"
                },
                "Analyze Impact on Existing Data": {
                    "start": "start_192",
                    "dead": "dead_192"
                },
                "Analyze Impact on User Workflows": {
                    "start": "start_193",
                    "dead": "dead_193"
                },
                "Analyze Impact on Integrations": {
                    "start": "start_194",
                    "dead": "dead_194"
                },
                "Analyze Impact on Reporting": {
                    "start": "start_195",
                    "dead": "dead_195"
                },
                "Analyze Impact on Analytics": {
                    "start": "start_196",
                    "dead": "dead_196"
                },
                "Analyze Impact on Security Rules": {
                    "start": "start_197",
                    "dead": "dead_197"
                },
                "Analyze Impact on Performance Requirements": {
                    "start": "start_198",
                    "dead": "dead_198"
                },
                "Analyze Impact on Error Handling": {
                    "start": "start_199",
                    "dead": "dead_199"
                },
                "Identify High-risk Change Areas": {
                    "start": "start_200",
                    "dead": "dead_200"
                },
                "Identify Required Refactor Scope": {
                    "start": "start_201",
                    "dead": "dead_201"
                },
                "Align Changes with Technical Constraints": {
                    "start": "start_202",
                    "dead": "dead_202"
                },
                "Align Changes with Product Vision": {
                    "start": "start_203",
                    "dead": "dead_203"
                },
                "Update Impact Analysis Document": {
                    "start": "start_204",
                    "dead": "dead_204"
                },
                "Review Impact Analysis with Tech Team": {
                    "start": "start_205",
                    "dead": "dead_205"
                },
                "Apply Feedback to Impact Analysis": {
                    "start": "start_206",
                    "dead": "dead_206"
                },
                "Sign Off Impact Analysis": {
                    "start": "start_207",
                    "dead": "dead_207"
                },
                "Re-align Roadmap Based on Changes": {
                    "start": "start_208",
                    "dead": "dead_208"
                },
                "Update Milestone Definitions": {
                    "start": "start_209",
                    "dead": "dead_209"
                },
                "Confirm Delivery Adjustments": {
                    "start": "start_210",
                    "dead": "dead_210"
                },
                "Communicate Changes to Stakeholders": {
                    "start": "start_211",
                    "dead": "dead_211"
                },
                "Confirm Refactor Readiness": {
                    "start": "start_212",
                    "dead": "dead_212"
                },
                "Finalize Change Alignment": {
                    "start": "start_213",
                    "dead": "dead_213"
                }
            },
            "Documentation & Approval": {
                "Update Business Requirement Document": {
                    "start": "start_214",
                    "dead": "dead_214"
                },
                "Update Business Rules Specification": {
                    "start": "start_215",
                    "dead": "dead_215"
                },
                "Update Process Flow Diagrams": {
                    "start": "start_216",
                    "dead": "dead_216"
                },
                "Update Data Definition Documents": {
                    "start": "start_217",
                    "dead": "dead_217"
                },
                "Update API-related BA Notes": {
                    "start": "start_218",
                    "dead": "dead_218"
                },
                "Review Updated Documents Internally": {
                    "start": "start_219",
                    "dead": "dead_219"
                },
                "Review Updated Documents with BE Team": {
                    "start": "start_220",
                    "dead": "dead_220"
                },
                "Review Updated Documents with FE Team": {
                    "start": "start_221",
                    "dead": "dead_221"
                },
                "Apply Review Feedback": {
                    "start": "start_222",
                    "dead": "dead_222"
                },
                "Resolve Documentation Conflicts": {
                    "start": "start_223",
                    "dead": "dead_223"
                },
                "Prepare Client Review Session": {
                    "start": "start_224",
                    "dead": "dead_224"
                },
                "Present Refactor Changes to Client": {
                    "start": "start_225",
                    "dead": "dead_225"
                },
                "Collect Client Feedback": {
                    "start": "start_226",
                    "dead": "dead_226"
                },
                "Apply Client Feedback": {
                    "start": "start_227",
                    "dead": "dead_227"
                },
                "Confirm Client Acceptance": {
                    "start": "start_228",
                    "dead": "dead_228"
                },
                "Finalize Approved Documents": {
                    "start": "start_229",
                    "dead": "dead_229"
                },
                "Archive Previous Versions": {
                    "start": "start_230",
                    "dead": "dead_230"
                },
                "Sign Off Client Requests #1": {
                    "start": "start_231",
                    "dead": "dead_231"
                },
                "Prepare Handover to Implementation": {
                    "start": "start_232",
                    "dead": "dead_232"
                },
                "Close Phase Client Requests #1": {
                    "start": "start_233",
                    "dead": "dead_233"
                }
            }
        },
        "Client Requests #2": {
            "Additional Change Requests": {
                "Analyze New Client Feedback Round": {
                    "start": "start_241",
                    "dead": "dead_241"
                },
                "Identify Late-stage Requirement Changes": {
                    "start": "start_242",
                    "dead": "dead_242"
                },
                "Clarify Urgent Business Adjustments": {
                    "start": "start_243",
                    "dead": "dead_243"
                },
                "Analyze Change Impact on Existing Refactor": {
                    "start": "start_244",
                    "dead": "dead_244"
                },
                "Identify Scope Creep Risks": {
                    "start": "start_245",
                    "dead": "dead_245"
                },
                "Negotiate Change Boundaries": {
                    "start": "start_246",
                    "dead": "dead_246"
                },
                "Update Priority Based on Urgency": {
                    "start": "start_247",
                    "dead": "dead_247"
                }
            }
        }
    }
}  # 247
QA_PROJECTS = {
    "CVWritingSupporter QualityAssurance": {
        "Main Services Quality Control": {
            "Functional Testing": {
                "Test User Authentication Flow": {
                    "start": "start_1",
                    "dead": "dead_1"
                },
                "Test User Registration Flow": {
                    "start": "start_2",
                    "dead": "dead_2"
                },
                "Test Login Error Scenarios": {
                    "start": "start_3",
                    "dead": "dead_3"
                },
                "Test Logout Behavior": {
                    "start": "start_4",
                    "dead": "dead_4"
                },
                "Test Role-based Access Control": {
                    "start": "start_5",
                    "dead": "dead_5"
                },
                "Test User Profile Retrieval": {
                    "start": "start_6",
                    "dead": "dead_6"
                },
                "Test User Profile Update": {
                    "start": "start_7",
                    "dead": "dead_7"
                },
                "Test CV Creation Flow": {
                    "start": "start_8",
                    "dead": "dead_8"
                },
                "Test CV Editing Flow": {
                    "start": "start_9",
                    "dead": "dead_9"
                },
                "Test CV Save Draft Functionality": {
                    "start": "start_10",
                    "dead": "dead_10"
                },
                "Test CV Submission Flow": {
                    "start": "start_11",
                    "dead": "dead_11"
                },
                "Test CV Validation Rules": {
                    "start": "start_12",
                    "dead": "dead_12"
                },
                "Test CV Parsing Results": {
                    "start": "start_13",
                    "dead": "dead_13"
                },
                "Test CV Scoring Logic": {
                    "start": "start_14",
                    "dead": "dead_14"
                },
                "Test CV Recommendation Output": {
                    "start": "start_15",
                    "dead": "dead_15"
                },
                "Test CV Version History": {
                    "start": "start_16",
                    "dead": "dead_16"
                },
                "Test CV Deletion Rules": {
                    "start": "start_17",
                    "dead": "dead_17"
                },
                "Test CV Visibility Rules": {
                    "start": "start_18",
                    "dead": "dead_18"
                },
                "Test CV Sharing Permissions": {
                    "start": "start_19",
                    "dead": "dead_19"
                },
                "Test Template Selection Flow": {
                    "start": "start_20",
                    "dead": "dead_20"
                },
                "Test Template Switching Behavior": {
                    "start": "start_21",
                    "dead": "dead_21"
                },
                "Test Template Rendering Accuracy": {
                    "start": "start_22",
                    "dead": "dead_22"
                },
                "Test API Request Validation": {
                    "start": "start_23",
                    "dead": "dead_23"
                },
                "Test API Response Mapping": {
                    "start": "start_24",
                    "dead": "dead_24"
                },
                "Test Error Message Display": {
                    "start": "start_25",
                    "dead": "dead_25"
                },
                "Test Form Validation Feedback": {
                    "start": "start_26",
                    "dead": "dead_26"
                },
                "Test Business Rule Enforcement": {
                    "start": "start_27",
                    "dead": "dead_27"
                },
                "Test Edge Case User Inputs": {
                    "start": "start_28",
                    "dead": "dead_28"
                },
                "Test Concurrent CV Editing": {
                    "start": "start_29",
                    "dead": "dead_29"
                },
                "Test Duplicate Submission Handling": {
                    "start": "start_30",
                    "dead": "dead_30"
                },
                "Test Notification Trigger Rules": {
                    "start": "start_31",
                    "dead": "dead_31"
                },
                "Test Audit Log Generation": {
                    "start": "start_32",
                    "dead": "dead_32"
                },
                "Test Data Persistence Accuracy": {
                    "start": "start_33",
                    "dead": "dead_33"
                },
                "Test Search & Filter Functions": {
                    "start": "start_34",
                    "dead": "dead_34"
                },
                "Test Pagination Behavior": {
                    "start": "start_35",
                    "dead": "dead_35"
                },
                "Test Sorting Logic": {
                    "start": "start_36",
                    "dead": "dead_36"
                },
                "Test Permission Denied Scenarios": {
                    "start": "start_37",
                    "dead": "dead_37"
                },
                "Test Invalid Token Handling": {
                    "start": "start_38",
                    "dead": "dead_38"
                },
                "Test Session Expiry Handling": {
                    "start": "start_39",
                    "dead": "dead_39"
                },
                "Sign Off Functional Testing": {
                    "start": "start_40",
                    "dead": "dead_40"
                }
            },
            "Integration & API Testing": {
                "Test BE–FE API Connectivity": {
                    "start": "start_41",
                    "dead": "dead_41"
                },
                "Test API Authentication Headers": {
                    "start": "start_42",
                    "dead": "dead_42"
                },
                "Test API Authorization Rules": {
                    "start": "start_43",
                    "dead": "dead_43"
                },
                "Test API Contract Compliance": {
                    "start": "start_44",
                    "dead": "dead_44"
                },
                "Test API Error Codes": {
                    "start": "start_45",
                    "dead": "dead_45"
                },
                "Test API Timeout Handling": {
                    "start": "start_46",
                    "dead": "dead_46"
                },
                "Test Retry Mechanism": {
                    "start": "start_47",
                    "dead": "dead_47"
                },
                "Test API Rate Limiting": {
                    "start": "start_48",
                    "dead": "dead_48"
                },
                "Test API Pagination Data": {
                    "start": "start_49",
                    "dead": "dead_49"
                },
                "Test API Sorting Parameters": {
                    "start": "start_50",
                    "dead": "dead_50"
                },
                "Test API Filtering Parameters": {
                    "start": "start_51",
                    "dead": "dead_51"
                },
                "Test API Payload Validation": {
                    "start": "start_52",
                    "dead": "dead_52"
                },
                "Test CV Upload API": {
                    "start": "start_53",
                    "dead": "dead_53"
                },
                "Test CV Parsing Integration": {
                    "start": "start_54",
                    "dead": "dead_54"
                },
                "Test CV Scoring Integration": {
                    "start": "start_55",
                    "dead": "dead_55"
                },
                "Test Recommendation API Integration": {
                    "start": "start_56",
                    "dead": "dead_56"
                },
                "Test External Service Failures": {
                    "start": "start_57",
                    "dead": "dead_57"
                },
                "Test Partial API Failure Scenarios": {
                    "start": "start_58",
                    "dead": "dead_58"
                },
                "Test Data Consistency Across Services": {
                    "start": "start_59",
                    "dead": "dead_59"
                },
                "Test Transaction Rollback Scenarios": {
                    "start": "start_60",
                    "dead": "dead_60"
                },
                "Test Concurrent API Requests": {
                    "start": "start_61",
                    "dead": "dead_61"
                },
                "Test API Idempotency": {
                    "start": "start_62",
                    "dead": "dead_62"
                },
                "Test Message Ordering": {
                    "start": "start_63",
                    "dead": "dead_63"
                },
                "Test API Versioning Support": {
                    "start": "start_64",
                    "dead": "dead_64"
                },
                "Test Deprecated API Behavior": {
                    "start": "start_65",
                    "dead": "dead_65"
                },
                "Test Logging of API Errors": {
                    "start": "start_66",
                    "dead": "dead_66"
                },
                "Test Monitoring Hooks": {
                    "start": "start_67",
                    "dead": "dead_67"
                },
                "Test API Security Vulnerabilities": {
                    "start": "start_68",
                    "dead": "dead_68"
                },
                "Test Injection Attack Protection": {
                    "start": "start_69",
                    "dead": "dead_69"
                },
                "Test Authorization Bypass Attempts": {
                    "start": "start_70",
                    "dead": "dead_70"
                },
                "Test API Load Under Stress": {
                    "start": "start_71",
                    "dead": "dead_71"
                },
                "Test API Graceful Degradation": {
                    "start": "start_72",
                    "dead": "dead_72"
                },
                "Test Integration with Analytics": {
                    "start": "start_73",
                    "dead": "dead_73"
                },
                "Test Reporting API Accuracy": {
                    "start": "start_74",
                    "dead": "dead_74"
                },
                "Test API Schema Validation": {
                    "start": "start_75",
                    "dead": "dead_75"
                },
                "Test API Backward Compatibility": {
                    "start": "start_76",
                    "dead": "dead_76"
                },
                "Test End-to-End API Flow": {
                    "start": "start_77",
                    "dead": "dead_77"
                },
                "Test Integration Regression": {
                    "start": "start_78",
                    "dead": "dead_78"
                },
                "Sign Off Integration Testing": {
                    "start": "start_79",
                    "dead": "dead_79"
                },
                "Finalize API Test Report": {
                    "start": "start_80",
                    "dead": "dead_80"
                }
            },
            "Non-functional Testing": {
                "Test System Performance Baseline": {
                    "start": "start_81",
                    "dead": "dead_81"
                },
                "Test Load Handling Capability": {
                    "start": "start_82",
                    "dead": "dead_82"
                },
                "Test Stress Conditions": {
                    "start": "start_83",
                    "dead": "dead_83"
                },
                "Test Peak Traffic Scenarios": {
                    "start": "start_84",
                    "dead": "dead_84"
                },
                "Test Response Time SLA": {
                    "start": "start_85",
                    "dead": "dead_85"
                },
                "Test Resource Utilization": {
                    "start": "start_86",
                    "dead": "dead_86"
                },
                "Test Memory Leak Scenarios": {
                    "start": "start_87",
                    "dead": "dead_87"
                },
                "Test CPU Usage Under Load": {
                    "start": "start_88",
                    "dead": "dead_88"
                },
                "Test Database Performance": {
                    "start": "start_89",
                    "dead": "dead_89"
                },
                "Test Cache Effectiveness": {
                    "start": "start_90",
                    "dead": "dead_90"
                },
                "Test Security Penetration Scenarios": {
                    "start": "start_91",
                    "dead": "dead_91"
                },
                "Test Authentication Brute-force Protection": {
                    "start": "start_92",
                    "dead": "dead_92"
                },
                "Test Authorization Escalation Attempts": {
                    "start": "start_93",
                    "dead": "dead_93"
                },
                "Test Data Encryption Compliance": {
                    "start": "start_94",
                    "dead": "dead_94"
                },
                "Test Sensitive Data Masking": {
                    "start": "start_95",
                    "dead": "dead_95"
                },
                "Test Logging Performance Impact": {
                    "start": "start_96",
                    "dead": "dead_96"
                },
                "Test Monitoring Alert Accuracy": {
                    "start": "start_97",
                    "dead": "dead_97"
                },
                "Test System Recovery Scenarios": {
                    "start": "start_98",
                    "dead": "dead_98"
                },
                "Test Failover Behavior": {
                    "start": "start_99",
                    "dead": "dead_99"
                },
                "Test Backup & Restore Process": {
                    "start": "start_100",
                    "dead": "dead_100"
                },
                "Test Browser Compatibility": {
                    "start": "start_101",
                    "dead": "dead_101"
                },
                "Test Mobile Responsiveness": {
                    "start": "start_102",
                    "dead": "dead_102"
                },
                "Test Cross-device Consistency": {
                    "start": "start_103",
                    "dead": "dead_103"
                },
                "Test Accessibility Compliance": {
                    "start": "start_104",
                    "dead": "dead_104"
                },
                "Test Localization & Language Support": {
                    "start": "start_105",
                    "dead": "dead_105"
                },
                "Test Timezone Handling": {
                    "start": "start_106",
                    "dead": "dead_106"
                },
                "Test Large Dataset Handling": {
                    "start": "start_107",
                    "dead": "dead_107"
                },
                "Test Long-running Session Stability": {
                    "start": "start_108",
                    "dead": "dead_108"
                },
                "Test Error Recovery UX": {
                    "start": "start_109",
                    "dead": "dead_109"
                },
                "Test Notification Delivery Performance": {
                    "start": "start_110",
                    "dead": "dead_110"
                },
                "Test Report Generation Performance": {
                    "start": "start_111",
                    "dead": "dead_111"
                },
                "Test Analytics Accuracy Under Load": {
                    "start": "start_112",
                    "dead": "dead_112"
                },
                "Test System Scalability Limits": {
                    "start": "start_113",
                    "dead": "dead_113"
                },
                "Test Cold Start Performance": {
                    "start": "start_114",
                    "dead": "dead_114"
                },
                "Test Graceful Shutdown": {
                    "start": "start_115",
                    "dead": "dead_115"
                },
                "Test Data Integrity After Failure": {
                    "start": "start_116",
                    "dead": "dead_116"
                },
                "Test End-to-End Stability": {
                    "start": "start_117",
                    "dead": "dead_117"
                },
                "Conduct QA Regression Round": {
                    "start": "start_118",
                    "dead": "dead_118"
                },
                "Finalize QA Test Summary": {
                    "start": "start_119",
                    "dead": "dead_119"
                },
                "Sign Off QA Phase": {
                    "start": "start_120",
                    "dead": "dead_120"
                }
            }
        },
        "Refactor Testing": {
            "Regression Testing After Refactor": {
                "Verify No Regression in Authentication Flow": {
                    "start": "start_121",
                    "dead": "dead_121"
                },
                "Verify No Regression in Authorization Rules": {
                    "start": "start_122",
                    "dead": "dead_122"
                },
                "Verify CV Creation After Refactor": {
                    "start": "start_123",
                    "dead": "dead_123"
                },
                "Verify CV Editing After Refactor": {
                    "start": "start_124",
                    "dead": "dead_124"
                },
                "Verify CV Submission After Refactor": {
                    "start": "start_125",
                    "dead": "dead_125"
                },
                "Verify CV Validation Rules After Refactor": {
                    "start": "start_126",
                    "dead": "dead_126"
                },
                "Verify CV Parsing Stability": {
                    "start": "start_127",
                    "dead": "dead_127"
                },
                "Verify CV Scoring Logic Integrity": {
                    "start": "start_128",
                    "dead": "dead_128"
                },
                "Verify Recommendation Output Consistency": {
                    "start": "start_129",
                    "dead": "dead_129"
                },
                "Verify CV Version History Integrity": {
                    "start": "start_130",
                    "dead": "dead_130"
                },
                "Verify Template Rendering After Refactor": {
                    "start": "start_131",
                    "dead": "dead_131"
                },
                "Verify Template Switching Behavior": {
                    "start": "start_132",
                    "dead": "dead_132"
                },
                "Verify User Profile Update Stability": {
                    "start": "start_133",
                    "dead": "dead_133"
                },
                "Verify Notification Triggers": {
                    "start": "start_134",
                    "dead": "dead_134"
                },
                "Verify Audit Log Generation": {
                    "start": "start_135",
                    "dead": "dead_135"
                },
                "Verify Data Persistence Consistency": {
                    "start": "start_136",
                    "dead": "dead_136"
                },
                "Verify Search Functionality": {
                    "start": "start_137",
                    "dead": "dead_137"
                },
                "Verify Filter Logic": {
                    "start": "start_138",
                    "dead": "dead_138"
                },
                "Verify Pagination Behavior": {
                    "start": "start_139",
                    "dead": "dead_139"
                },
                "Verify Sorting Rules": {
                    "start": "start_140",
                    "dead": "dead_140"
                },
                "Verify Error Message Accuracy": {
                    "start": "start_141",
                    "dead": "dead_141"
                },
                "Verify Form Validation UX": {
                    "start": "start_142",
                    "dead": "dead_142"
                },
                "Verify Permission Enforcement": {
                    "start": "start_143",
                    "dead": "dead_143"
                },
                "Verify Session Handling": {
                    "start": "start_144",
                    "dead": "dead_144"
                },
                "Verify Token Expiry Handling": {
                    "start": "start_145",
                    "dead": "dead_145"
                },
                "Verify Concurrent User Actions": {
                    "start": "start_146",
                    "dead": "dead_146"
                },
                "Verify Duplicate Submission Prevention": {
                    "start": "start_147",
                    "dead": "dead_147"
                },
                "Verify Business Rule Execution Order": {
                    "start": "start_148",
                    "dead": "dead_148"
                },
                "Verify Logging Format Stability": {
                    "start": "start_149",
                    "dead": "dead_149"
                },
                "Verify Monitoring Metrics": {
                    "start": "start_150",
                    "dead": "dead_150"
                },
                "Verify Reporting Data Accuracy": {
                    "start": "start_151",
                    "dead": "dead_151"
                },
                "Verify Analytics Event Tracking": {
                    "start": "start_152",
                    "dead": "dead_152"
                },
                "Verify API Backward Compatibility": {
                    "start": "start_153",
                    "dead": "dead_153"
                },
                "Verify Deprecated API Behavior": {
                    "start": "start_154",
                    "dead": "dead_154"
                },
                "Verify End-to-End User Flow": {
                    "start": "start_155",
                    "dead": "dead_155"
                },
                "Verify Cross-Domain Interaction Stability": {
                    "start": "start_156",
                    "dead": "dead_156"
                },
                "Verify Refactor Regression Coverage": {
                    "start": "start_157",
                    "dead": "dead_157"
                },
                "Execute Full Regression Suite": {
                    "start": "start_158",
                    "dead": "dead_158"
                },
                "Analyze Regression Test Results": {
                    "start": "start_159",
                    "dead": "dead_159"
                },
                "Sign Off Regression Testing": {
                    "start": "start_160",
                    "dead": "dead_160"
                }
            },
            "API & Integration Testing After Refactor": {
                "Verify API Contract Post-Refactor": {
                    "start": "start_161",
                    "dead": "dead_161"
                },
                "Verify API Request Validation": {
                    "start": "start_162",
                    "dead": "dead_162"
                },
                "Verify API Response Mapping": {
                    "start": "start_163",
                    "dead": "dead_163"
                },
                "Verify API Error Code Consistency": {
                    "start": "start_164",
                    "dead": "dead_164"
                },
                "Verify API Authorization Rules": {
                    "start": "start_165",
                    "dead": "dead_165"
                },
                "Verify API Authentication Flow": {
                    "start": "start_166",
                    "dead": "dead_166"
                },
                "Verify API Pagination Parameters": {
                    "start": "start_167",
                    "dead": "dead_167"
                },
                "Verify API Filtering Parameters": {
                    "start": "start_168",
                    "dead": "dead_168"
                },
                "Verify API Sorting Parameters": {
                    "start": "start_169",
                    "dead": "dead_169"
                },
                "Verify API Payload Structure": {
                    "start": "start_170",
                    "dead": "dead_170"
                },
                "Verify CV Upload API After Refactor": {
                    "start": "start_171",
                    "dead": "dead_171"
                },
                "Verify CV Parsing API Integration": {
                    "start": "start_172",
                    "dead": "dead_172"
                },
                "Verify Scoring API Integration": {
                    "start": "start_173",
                    "dead": "dead_173"
                },
                "Verify Recommendation API Integration": {
                    "start": "start_174",
                    "dead": "dead_174"
                },
                "Verify External Service Integration": {
                    "start": "start_175",
                    "dead": "dead_175"
                },
                "Verify Partial Failure Handling": {
                    "start": "start_176",
                    "dead": "dead_176"
                },
                "Verify Transaction Rollback Logic": {
                    "start": "start_177",
                    "dead": "dead_177"
                },
                "Verify Concurrent API Requests": {
                    "start": "start_178",
                    "dead": "dead_178"
                },
                "Verify API Idempotency": {
                    "start": "start_179",
                    "dead": "dead_179"
                },
                "Verify Message Ordering": {
                    "start": "start_180",
                    "dead": "dead_180"
                },
                "Verify API Versioning Rules": {
                    "start": "start_181",
                    "dead": "dead_181"
                },
                "Verify API Logging Behavior": {
                    "start": "start_182",
                    "dead": "dead_182"
                },
                "Verify Security Headers": {
                    "start": "start_183",
                    "dead": "dead_183"
                },
                "Verify Injection Attack Protection": {
                    "start": "start_184",
                    "dead": "dead_184"
                },
                "Verify Authorization Bypass Protection": {
                    "start": "start_185",
                    "dead": "dead_185"
                },
                "Verify API Performance Under Load": {
                    "start": "start_186",
                    "dead": "dead_186"
                },
                "Verify API Timeout Handling": {
                    "start": "start_187",
                    "dead": "dead_187"
                },
                "Verify Retry Mechanism": {
                    "start": "start_188",
                    "dead": "dead_188"
                },
                "Verify Rate Limiting Rules": {
                    "start": "start_189",
                    "dead": "dead_189"
                },
                "Verify API Graceful Degradation": {
                    "start": "start_190",
                    "dead": "dead_190"
                },
                "Verify API Monitoring Hooks": {
                    "start": "start_191",
                    "dead": "dead_191"
                },
                "Verify API Metrics Accuracy": {
                    "start": "start_192",
                    "dead": "dead_192"
                },
                "Verify Reporting API Accuracy": {
                    "start": "start_193",
                    "dead": "dead_193"
                },
                "Verify Analytics API Data": {
                    "start": "start_194",
                    "dead": "dead_194"
                },
                "Verify End-to-End API Flow": {
                    "start": "start_195",
                    "dead": "dead_195"
                },
                "Execute Integration Test Suite": {
                    "start": "start_196",
                    "dead": "dead_196"
                },
                "Analyze Integration Test Results": {
                    "start": "start_197",
                    "dead": "dead_197"
                },
                "Sign Off Integration Refactor Testing": {
                    "start": "start_198",
                    "dead": "dead_198"
                },
                "Finalize API Refactor Test Report": {
                    "start": "start_199",
                    "dead": "dead_199"
                },
                "Close Integration Testing Phase": {
                    "start": "start_200",
                    "dead": "dead_200"
                }
            },
            "Non-functional & Stability Testing After Refactor": {
                "Verify Performance Baseline After Refactor": {
                    "start": "start_201",
                    "dead": "dead_201"
                },
                "Verify Load Handling After Refactor": {
                    "start": "start_202",
                    "dead": "dead_202"
                },
                "Verify Stress Handling": {
                    "start": "start_203",
                    "dead": "dead_203"
                },
                "Verify Peak Traffic Stability": {
                    "start": "start_204",
                    "dead": "dead_204"
                },
                "Verify Response Time SLA": {
                    "start": "start_205",
                    "dead": "dead_205"
                },
                "Verify Resource Utilization": {
                    "start": "start_206",
                    "dead": "dead_206"
                },
                "Verify Memory Stability": {
                    "start": "start_207",
                    "dead": "dead_207"
                },
                "Verify CPU Usage Stability": {
                    "start": "start_208",
                    "dead": "dead_208"
                },
                "Verify Database Performance": {
                    "start": "start_209",
                    "dead": "dead_209"
                },
                "Verify Cache Effectiveness": {
                    "start": "start_210",
                    "dead": "dead_210"
                },
                "Verify Security Compliance": {
                    "start": "start_211",
                    "dead": "dead_211"
                },
                "Verify Authentication Attack Resistance": {
                    "start": "start_212",
                    "dead": "dead_212"
                },
                "Verify Authorization Escalation Protection": {
                    "start": "start_213",
                    "dead": "dead_213"
                },
                "Verify Data Encryption Integrity": {
                    "start": "start_214",
                    "dead": "dead_214"
                },
                "Verify Sensitive Data Masking": {
                    "start": "start_215",
                    "dead": "dead_215"
                },
                "Verify Logging Performance Impact": {
                    "start": "start_216",
                    "dead": "dead_216"
                },
                "Verify Monitoring Alert Accuracy": {
                    "start": "start_217",
                    "dead": "dead_217"
                },
                "Verify System Recovery Scenarios": {
                    "start": "start_218",
                    "dead": "dead_218"
                },
                "Verify Failover Behavior": {
                    "start": "start_219",
                    "dead": "dead_219"
                },
                "Verify Backup & Restore Stability": {
                    "start": "start_220",
                    "dead": "dead_220"
                },
                "Verify Browser Compatibility After Refactor": {
                    "start": "start_221",
                    "dead": "dead_221"
                },
                "Verify Mobile Responsiveness After Refactor": {
                    "start": "start_222",
                    "dead": "dead_222"
                },
                "Verify Accessibility Compliance": {
                    "start": "start_223",
                    "dead": "dead_223"
                },
                "Verify Localization Stability": {
                    "start": "start_224",
                    "dead": "dead_224"
                },
                "Verify Timezone Handling": {
                    "start": "start_225",
                    "dead": "dead_225"
                },
                "Verify Large Dataset Handling": {
                    "start": "start_226",
                    "dead": "dead_226"
                },
                "Verify Long-running Session Stability": {
                    "start": "start_227",
                    "dead": "dead_227"
                },
                "Verify Error Recovery UX": {
                    "start": "start_228",
                    "dead": "dead_228"
                },
                "Verify Notification Delivery Performance": {
                    "start": "start_229",
                    "dead": "dead_229"
                },
                "Verify Report Generation Performance": {
                    "start": "start_230",
                    "dead": "dead_230"
                },
                "Verify Analytics Accuracy Under Load": {
                    "start": "start_231",
                    "dead": "dead_231"
                },
                "Verify System Scalability Limits": {
                    "start": "start_232",
                    "dead": "dead_232"
                },
                "Verify Cold Start Performance": {
                    "start": "start_233",
                    "dead": "dead_233"
                },
                "Verify Graceful Shutdown Behavior": {
                    "start": "start_234",
                    "dead": "dead_234"
                },
                "Verify Data Integrity After Failure": {
                    "start": "start_235",
                    "dead": "dead_235"
                },
                "Verify End-to-End Stability After Refactor": {
                    "start": "start_236",
                    "dead": "dead_236"
                },
                "Execute Stability Test Suite": {
                    "start": "start_237",
                    "dead": "dead_237"
                },
                "Analyze Stability Test Results": {
                    "start": "start_238",
                    "dead": "dead_238"
                },
                "Fix Blocking Issues Identified": {
                    "start": "start_239",
                    "dead": "dead_239"
                },
                "Re-test Fixed Stability Issues": {
                    "start": "start_240",
                    "dead": "dead_240"
                },
                "Final QA Regression After Refactor": {
                    "start": "start_241",
                    "dead": "dead_241"
                },
                "Prepare QA Refactor Summary": {
                    "start": "start_242",
                    "dead": "dead_242"
                },
                "Review QA Exit Criteria": {
                    "start": "start_243",
                    "dead": "dead_243"
                },
                "Final QA Approval": {
                    "start": "start_244",
                    "dead": "dead_244"
                },
                "Sign Off Refactor Testing": {
                    "start": "start_245",
                    "dead": "dead_245"
                },
                "Archive Test Artifacts": {
                    "start": "start_246",
                    "dead": "dead_246"
                },
                "Close QA Refactor Phase": {
                    "start": "start_247",
                    "dead": "dead_247"
                }
            }
        },
        "Post-Refactor & Release Validation": {
            "UAT & Business Validation": {
                "Validate User Acceptance Scenarios": {
                    "start": "start_248",
                    "dead": "dead_248"
                },
                "Validate End-user CV Creation Journey": {
                    "start": "start_249",
                    "dead": "dead_249"
                },
                "Validate CV Submission Approval Flow": {
                    "start": "start_250",
                    "dead": "dead_250"
                },
                "Validate CV Recommendation Usefulness": {
                    "start": "start_251",
                    "dead": "dead_251"
                },
                "Validate Role-based User Journeys": {
                    "start": "start_252",
                    "dead": "dead_252"
                },
                "Validate Business Rule Interpretation": {
                    "start": "start_253",
                    "dead": "dead_253"
                },
                "Validate Error Handling from User Perspective": {
                    "start": "start_254",
                    "dead": "dead_254"
                },
                "Validate Edge Case Business Scenarios": {
                    "start": "start_255",
                    "dead": "dead_255"
                },
                "Validate CV Template User Experience": {
                    "start": "start_256",
                    "dead": "dead_256"
                },
                "Sign Off User Acceptance Testing": {
                    "start": "start_257",
                    "dead": "dead_257"
                }
            },

            "Production Readiness Testing": {
                "Verify Production Configuration Consistency": {
                    "start": "start_258",
                    "dead": "dead_258"
                },
                "Verify Feature Flags Configuration": {
                    "start": "start_259",
                    "dead": "dead_259"
                },
                "Verify Logging Level in Production Mode": {
                    "start": "start_260",
                    "dead": "dead_260"
                },
                "Verify Monitoring Dashboards": {
                    "start": "start_261",
                    "dead": "dead_261"
                },
                "Verify Alerting Rules": {
                    "start": "start_262",
                    "dead": "dead_262"
                },
                "Verify Backup Jobs Configuration": {
                    "start": "start_263",
                    "dead": "dead_263"
                },
                "Verify Data Migration Safety": {
                    "start": "start_264",
                    "dead": "dead_264"
                },
                "Verify Rollback Plan Execution": {
                    "start": "start_265",
                    "dead": "dead_265"
                },
                "Verify Deployment Smoke Tests": {
                    "start": "start_266",
                    "dead": "dead_266"
                },
                "Approve Production Readiness": {
                    "start": "start_267",
                    "dead": "dead_267"
                }
            },

            "Post-deployment Validation": {
                "Execute Production Smoke Testing": {
                    "start": "start_268",
                    "dead": "dead_268"
                },
                "Validate Live User Authentication": {
                    "start": "start_269",
                    "dead": "dead_269"
                },
                "Validate Live CV Submission": {
                    "start": "start_270",
                    "dead": "dead_270"
                },
                "Validate Live CV Parsing Output": {
                    "start": "start_271",
                    "dead": "dead_271"
                },
                "Validate Live Recommendation Results": {
                    "start": "start_272",
                    "dead": "dead_272"
                },
                "Validate Monitoring Metrics After Release": {
                    "start": "start_273",
                    "dead": "dead_273"
                },
                "Validate Error Rate Thresholds": {
                    "start": "start_274",
                    "dead": "dead_274"
                },
                "Validate Performance Under Real Traffic": {
                    "start": "start_275",
                    "dead": "dead_275"
                },
                "Validate No Critical Incident in First 24h": {
                    "start": "start_276",
                    "dead": "dead_276"
                }
            },

            "QA Closure & Reporting": {
                "Collect QA Metrics Summary": {
                    "start": "start_277",
                    "dead": "dead_277"
                },
                "Analyze Production Issues Feedback": {
                    "start": "start_278",
                    "dead": "dead_278"
                },
                "Confirm No Critical Open Defects": {
                    "start": "start_279",
                    "dead": "dead_279"
                },
                "Finalize QA Release Report": {
                    "start": "start_280",
                    "dead": "dead_280"
                },
                "Review QA Lessons Learned": {
                    "start": "start_281",
                    "dead": "dead_281"
                },
                "Archive QA Artifacts": {
                    "start": "start_282",
                    "dead": "dead_282"
                },
                "Close QA Release Phase": {
                    "start": "start_283",
                    "dead": "dead_283"
                },
                "Final QA Sign-off": {
                    "start": "start_284",
                    "dead": "dead_284"
                },
                "Support Post-release Monitoring": {
                    "start": "start_285",
                    "dead": "dead_285"
                },
                "Confirm System Stability After Release": {
                    "start": "start_286",
                    "dead": "dead_286"
                }
            },

            "Extended QA Safeguards": {
                "Validate Long-term Session Stability": {
                    "start": "start_287",
                    "dead": "dead_287"
                },
                "Validate Data Retention Rules": {
                    "start": "start_288",
                    "dead": "dead_288"
                },
                "Validate Audit Trail Completeness": {
                    "start": "start_289",
                    "dead": "dead_289"
                },
                "Validate Compliance Evidence Collection": {
                    "start": "start_290",
                    "dead": "dead_290"
                },
                "Validate Cross-region Behavior": {
                    "start": "start_291",
                    "dead": "dead_291"
                },
                "Validate Disaster Recovery Drill": {
                    "start": "start_292",
                    "dead": "dead_292"
                },
                "Final QA Project Closure": {
                    "start": "start_293",
                    "dead": "dead_293"
                },
                "QA Executive Sign-off": {
                    "start": "start_294",
                    "dead": "dead_294"
                }
            }
        }
    }
}  # 294
HR_PROJECTS = {
    "CVWritingSupporter HumanResources": {
        "Onsite & Employee Documentation": {
            "Onsite Preparation Documents": {
                "Collect Employee Personal Documents": {
                    "start": "start_1",
                    "dead": "dead_1"
                },
                "Verify Employee ID Copies": {
                    "start": "start_2",
                    "dead": "dead_2"
                },
                "Prepare Passport Scan Files": {
                    "start": "start_3",
                    "dead": "dead_3"
                },
                "Collect Visa Application Forms": {
                    "start": "start_4",
                    "dead": "dead_4"
                },
                "Review Visa Supporting Documents": {
                    "start": "start_5",
                    "dead": "dead_5"
                },
                "Prepare Onsite Invitation Letters": {
                    "start": "start_6",
                    "dead": "dead_6"
                },
                "Collect Employment Contracts": {
                    "start": "start_7",
                    "dead": "dead_7"
                },
                "Verify Contract Validity Period": {
                    "start": "start_8",
                    "dead": "dead_8"
                },
                "Prepare Assignment Decision Documents": {
                    "start": "start_9",
                    "dead": "dead_9"
                },
                "Collect Health Check Certificates": {
                    "start": "start_10",
                    "dead": "dead_10"
                },
                "Verify Insurance Coverage": {
                    "start": "start_11",
                    "dead": "dead_11"
                },
                "Prepare Onsite Policy Documents": {
                    "start": "start_12",
                    "dead": "dead_12"
                },
                "Compile Onsite Checklist": {
                    "start": "start_13",
                    "dead": "dead_13"
                },
                "Review Country-specific Regulations": {
                    "start": "start_14",
                    "dead": "dead_14"
                },
                "Prepare Travel Authorization Forms": {
                    "start": "start_15",
                    "dead": "dead_15"
                },
                "Collect Emergency Contact Forms": {
                    "start": "start_16",
                    "dead": "dead_16"
                },
                "Verify Employee Availability": {
                    "start": "start_17",
                    "dead": "dead_17"
                },
                "Confirm Onsite Duration": {
                    "start": "start_18",
                    "dead": "dead_18"
                },
                "Prepare Onsite Timeline Document": {
                    "start": "start_19",
                    "dead": "dead_19"
                },
                "Send Onsite Preparation Emails": {
                    "start": "start_20",
                    "dead": "dead_20"
                },
                "Collect Signed Commitments": {
                    "start": "start_21",
                    "dead": "dead_21"
                },
                "Archive Submitted Documents": {
                    "start": "start_22",
                    "dead": "dead_22"
                },
                "Verify Document Completeness": {
                    "start": "start_23",
                    "dead": "dead_23"
                },
                "Resolve Missing Document Issues": {
                    "start": "start_24",
                    "dead": "dead_24"
                },
                "Prepare Final Onsite Dossier": {
                    "start": "start_25",
                    "dead": "dead_25"
                },
                "Internal Review of Onsite Files": {
                    "start": "start_26",
                    "dead": "dead_26"
                },
                "Submit Documents to Management": {
                    "start": "start_27",
                    "dead": "dead_27"
                },
                "Update Onsite Status Tracker": {
                    "start": "start_28",
                    "dead": "dead_28"
                },
                "Confirm Approval from Stakeholders": {
                    "start": "start_29",
                    "dead": "dead_29"
                },
                "Notify Employees of Approval": {
                    "start": "start_30",
                    "dead": "dead_30"
                },
                "Finalize Onsite Documentation": {
                    "start": "start_31",
                    "dead": "dead_31"
                },
                "Sign Off Onsite Documents": {
                    "start": "start_32",
                    "dead": "dead_32"
                },
                "Close Onsite Documentation Phase": {
                    "start": "start_33",
                    "dead": "dead_33"
                }
            },
            "Meeting & Communication Reports": {
                "Prepare Meeting Agenda Template": {
                    "start": "start_34",
                    "dead": "dead_34"
                },
                "Collect Meeting Notes": {
                    "start": "start_35",
                    "dead": "dead_35"
                },
                "Draft Weekly HR Meeting Report": {
                    "start": "start_36",
                    "dead": "dead_36"
                },
                "Draft Monthly HR Meeting Summary": {
                    "start": "start_37",
                    "dead": "dead_37"
                },
                "Compile Action Items List": {
                    "start": "start_38",
                    "dead": "dead_38"
                },
                "Assign Action Items to Owners": {
                    "start": "start_39",
                    "dead": "dead_39"
                },
                "Track Action Item Progress": {
                    "start": "start_40",
                    "dead": "dead_40"
                },
                "Prepare Follow-up Meeting Notes": {
                    "start": "start_41",
                    "dead": "dead_41"
                },
                "Draft Cross-team Meeting Report": {
                    "start": "start_42",
                    "dead": "dead_42"
                },
                "Summarize Management Decisions": {
                    "start": "start_43",
                    "dead": "dead_43"
                },
                "Prepare Stakeholder Communication": {
                    "start": "start_44",
                    "dead": "dead_44"
                },
                "Review Report Accuracy": {
                    "start": "start_45",
                    "dead": "dead_45"
                },
                "Revise Meeting Report Content": {
                    "start": "start_46",
                    "dead": "dead_46"
                },
                "Format Official Meeting Report": {
                    "start": "start_47",
                    "dead": "dead_47"
                },
                "Send Meeting Report to Attendees": {
                    "start": "start_48",
                    "dead": "dead_48"
                },
                "Archive Meeting Reports": {
                    "start": "start_49",
                    "dead": "dead_49"
                },
                "Prepare Quarterly HR Review Notes": {
                    "start": "start_50",
                    "dead": "dead_50"
                },
                "Document HR Policy Discussions": {
                    "start": "start_51",
                    "dead": "dead_51"
                },
                "Summarize Employee Feedback": {
                    "start": "start_52",
                    "dead": "dead_52"
                },
                "Prepare Decision Log": {
                    "start": "start_53",
                    "dead": "dead_53"
                },
                "Verify Meeting Attendance Records": {
                    "start": "start_54",
                    "dead": "dead_54"
                },
                "Prepare Executive Briefing Notes": {
                    "start": "start_55",
                    "dead": "dead_55"
                },
                "Review Communication Tone": {
                    "start": "start_56",
                    "dead": "dead_56"
                },
                "Align Report with HR Standards": {
                    "start": "start_57",
                    "dead": "dead_57"
                },
                "Resolve Missing Information": {
                    "start": "start_58",
                    "dead": "dead_58"
                },
                "Finalize Meeting Reports": {
                    "start": "start_59",
                    "dead": "dead_59"
                },
                "Sign Off Meeting Documentation": {
                    "start": "start_60",
                    "dead": "dead_60"
                },
                "Publish Internal HR Reports": {
                    "start": "start_61",
                    "dead": "dead_61"
                },
                "Notify Relevant Departments": {
                    "start": "start_62",
                    "dead": "dead_62"
                },
                "Store Reports in HR System": {
                    "start": "start_63",
                    "dead": "dead_63"
                },
                "Audit Meeting Documentation": {
                    "start": "start_64",
                    "dead": "dead_64"
                },
                "Close Meeting Report Collection": {
                    "start": "start_65",
                    "dead": "dead_65"
                },
                "Complete Communication Review": {
                    "start": "start_66",
                    "dead": "dead_66"
                }
            },
            "Employee Records & Compliance": {
                "Update Employee Personal Records": {
                    "start": "start_67",
                    "dead": "dead_67"
                },
                "Verify Employee Contact Information": {
                    "start": "start_68",
                    "dead": "dead_68"
                },
                "Maintain Employment History Files": {
                    "start": "start_69",
                    "dead": "dead_69"
                },
                "Review Labor Contract Compliance": {
                    "start": "start_70",
                    "dead": "dead_70"
                },
                "Update Job Title Records": {
                    "start": "start_71",
                    "dead": "dead_71"
                },
                "Update Department Assignment": {
                    "start": "start_72",
                    "dead": "dead_72"
                },
                "Track Employee Status Changes": {
                    "start": "start_73",
                    "dead": "dead_73"
                },
                "Archive Resigned Employee Files": {
                    "start": "start_74",
                    "dead": "dead_74"
                },
                "Prepare Compliance Audit Files": {
                    "start": "start_75",
                    "dead": "dead_75"
                },
                "Verify Legal Document Storage": {
                    "start": "start_76",
                    "dead": "dead_76"
                },
                "Review Data Privacy Compliance": {
                    "start": "start_77",
                    "dead": "dead_77"
                },
                "Prepare HR Compliance Checklist": {
                    "start": "start_78",
                    "dead": "dead_78"
                },
                "Conduct Internal HR Audit": {
                    "start": "start_79",
                    "dead": "dead_79"
                },
                "Resolve Compliance Gaps": {
                    "start": "start_80",
                    "dead": "dead_80"
                },
                "Document Audit Findings": {
                    "start": "start_81",
                    "dead": "dead_81"
                },
                "Prepare Audit Summary Report": {
                    "start": "start_82",
                    "dead": "dead_82"
                },
                "Submit Compliance Report": {
                    "start": "start_83",
                    "dead": "dead_83"
                },
                "Update HR Policies Documentation": {
                    "start": "start_84",
                    "dead": "dead_84"
                },
                "Communicate Policy Updates": {
                    "start": "start_85",
                    "dead": "dead_85"
                },
                "Collect Policy Acknowledgements": {
                    "start": "start_86",
                    "dead": "dead_86"
                },
                "Verify Acknowledgement Completion": {
                    "start": "start_87",
                    "dead": "dead_87"
                },
                "Archive Policy Documents": {
                    "start": "start_88",
                    "dead": "dead_88"
                },
                "Prepare Compliance Training Materials": {
                    "start": "start_89",
                    "dead": "dead_89"
                },
                "Record Training Attendance": {
                    "start": "start_90",
                    "dead": "dead_90"
                },
                "Evaluate Training Effectiveness": {
                    "start": "start_91",
                    "dead": "dead_91"
                },
                "Update Compliance Metrics": {
                    "start": "start_92",
                    "dead": "dead_92"
                },
                "Review Regulatory Changes": {
                    "start": "start_93",
                    "dead": "dead_93"
                },
                "Adjust HR Procedures": {
                    "start": "start_94",
                    "dead": "dead_94"
                },
                "Finalize Compliance Records": {
                    "start": "start_95",
                    "dead": "dead_95"
                },
                "Sign Off Compliance Documentation": {
                    "start": "start_96",
                    "dead": "dead_96"
                },
                "Close Compliance Collection": {
                    "start": "start_97",
                    "dead": "dead_97"
                },
                "Complete Employee Records Review": {
                    "start": "start_98",
                    "dead": "dead_98"
                },
                "Archive Final HR Records": {
                    "start": "start_99",
                    "dead": "dead_99"
                }
            }
        },
        "Compensation & HR Reporting": {
            "Salary & Allowance Reports": {
                "Collect Monthly Salary Data": {
                    "start": "start_100",
                    "dead": "dead_100"
                },
                "Verify Salary Calculation Sheets": {
                    "start": "start_101",
                    "dead": "dead_101"
                },
                "Prepare Quarterly Salary Report": {
                    "start": "start_102",
                    "dead": "dead_102"
                },
                "Analyze Salary Adjustment History": {
                    "start": "start_103",
                    "dead": "dead_103"
                },
                "Compile Allowance Records": {
                    "start": "start_104",
                    "dead": "dead_104"
                },
                "Verify Overtime Payment Data": {
                    "start": "start_105",
                    "dead": "dead_105"
                },
                "Prepare Bonus Distribution Report": {
                    "start": "start_106",
                    "dead": "dead_106"
                },
                "Review Payroll Discrepancies": {
                    "start": "start_107",
                    "dead": "dead_107"
                },
                "Resolve Salary Data Issues": {
                    "start": "start_108",
                    "dead": "dead_108"
                },
                "Generate Salary Trend Analysis": {
                    "start": "start_109",
                    "dead": "dead_109"
                },
                "Prepare Department Salary Breakdown": {
                    "start": "start_110",
                    "dead": "dead_110"
                },
                "Review Cost Allocation": {
                    "start": "start_111",
                    "dead": "dead_111"
                },
                "Prepare Management Salary Summary": {
                    "start": "start_112",
                    "dead": "dead_112"
                },
                "Validate Payroll Approval": {
                    "start": "start_113",
                    "dead": "dead_113"
                },
                "Document Payroll Assumptions": {
                    "start": "start_114",
                    "dead": "dead_114"
                },
                "Review Compensation Policies": {
                    "start": "start_115",
                    "dead": "dead_115"
                },
                "Update Salary Bands": {
                    "start": "start_116",
                    "dead": "dead_116"
                },
                "Verify Market Benchmark Data": {
                    "start": "start_117",
                    "dead": "dead_117"
                },
                "Prepare Compensation Adjustment Proposal": {
                    "start": "start_118",
                    "dead": "dead_118"
                },
                "Collect Management Feedback": {
                    "start": "start_119",
                    "dead": "dead_119"
                },
                "Revise Salary Reports": {
                    "start": "start_120",
                    "dead": "dead_120"
                },
                "Finalize Salary Reports": {
                    "start": "start_121",
                    "dead": "dead_121"
                },
                "Submit Salary Reports for Approval": {
                    "start": "start_122",
                    "dead": "dead_122"
                },
                "Record Approved Salary Changes": {
                    "start": "start_123",
                    "dead": "dead_123"
                },
                "Communicate Salary Updates": {
                    "start": "start_124",
                    "dead": "dead_124"
                },
                "Archive Salary Documentation": {
                    "start": "start_125",
                    "dead": "dead_125"
                },
                "Prepare Annual Salary Summary": {
                    "start": "start_126",
                    "dead": "dead_126"
                },
                "Review Compensation KPIs": {
                    "start": "start_127",
                    "dead": "dead_127"
                },
                "Audit Salary Data Accuracy": {
                    "start": "start_128",
                    "dead": "dead_128"
                },
                "Sign Off Salary Reports": {
                    "start": "start_129",
                    "dead": "dead_129"
                },
                "Close Salary Report Collection": {
                    "start": "start_130",
                    "dead": "dead_130"
                },
                "Complete Compensation Review": {
                    "start": "start_131",
                    "dead": "dead_131"
                },
                "Archive Final Compensation Files": {
                    "start": "start_132",
                    "dead": "dead_132"
                }
            },
            "HR Metrics & Statistics Reports": {
                "Collect Headcount Data": {
                    "start": "start_133",
                    "dead": "dead_133"
                },
                "Prepare Monthly Headcount Report": {
                    "start": "start_134",
                    "dead": "dead_134"
                },
                "Analyze Headcount Changes": {
                    "start": "start_135",
                    "dead": "dead_135"
                },
                "Prepare Turnover Rate Statistics": {
                    "start": "start_136",
                    "dead": "dead_136"
                },
                "Analyze Attrition Trends": {
                    "start": "start_137",
                    "dead": "dead_137"
                },
                "Prepare Recruitment Pipeline Report": {
                    "start": "start_138",
                    "dead": "dead_138"
                },
                "Collect Hiring Data": {
                    "start": "start_139",
                    "dead": "dead_139"
                },
                "Prepare Time-to-Hire Metrics": {
                    "start": "start_140",
                    "dead": "dead_140"
                },
                "Analyze Recruitment Efficiency": {
                    "start": "start_141",
                    "dead": "dead_141"
                },
                "Prepare Training Participation Report": {
                    "start": "start_142",
                    "dead": "dead_142"
                },
                "Collect Training Cost Data": {
                    "start": "start_143",
                    "dead": "dead_143"
                },
                "Analyze Training Effectiveness": {
                    "start": "start_144",
                    "dead": "dead_144"
                },
                "Prepare Absence Statistics": {
                    "start": "start_145",
                    "dead": "dead_145"
                },
                "Analyze Leave Patterns": {
                    "start": "start_146",
                    "dead": "dead_146"
                },
                "Prepare Overtime Statistics": {
                    "start": "start_147",
                    "dead": "dead_147"
                },
                "Analyze Workforce Utilization": {
                    "start": "start_148",
                    "dead": "dead_148"
                },
                "Prepare Gender Diversity Metrics": {
                    "start": "start_149",
                    "dead": "dead_149"
                },
                "Prepare Age Distribution Report": {
                    "start": "start_150",
                    "dead": "dead_150"
                },
                "Prepare Skill Distribution Report": {
                    "start": "start_151",
                    "dead": "dead_151"
                },
                "Analyze Workforce Composition": {
                    "start": "start_152",
                    "dead": "dead_152"
                },
                "Prepare Quarterly HR Dashboard": {
                    "start": "start_153",
                    "dead": "dead_153"
                },
                "Validate HR Metric Accuracy": {
                    "start": "start_154",
                    "dead": "dead_154"
                },
                "Review KPI Definitions": {
                    "start": "start_155",
                    "dead": "dead_155"
                },
                "Update Metrics Documentation": {
                    "start": "start_156",
                    "dead": "dead_156"
                },
                "Prepare Management Metrics Summary": {
                    "start": "start_157",
                    "dead": "dead_157"
                },
                "Collect Management Feedback": {
                    "start": "start_158",
                    "dead": "dead_158"
                },
                "Revise Metrics Reports": {
                    "start": "start_159",
                    "dead": "dead_159"
                },
                "Finalize HR Metrics Reports": {
                    "start": "start_160",
                    "dead": "dead_160"
                },
                "Publish HR Statistics": {
                    "start": "start_161",
                    "dead": "dead_161"
                },
                "Archive Metrics Documentation": {
                    "start": "start_162",
                    "dead": "dead_162"
                },
                "Sign Off HR Metrics Reports": {
                    "start": "start_163",
                    "dead": "dead_163"
                },
                "Close Metrics Collection": {
                    "start": "start_164",
                    "dead": "dead_164"
                },
                "Complete HR Statistics Review": {
                    "start": "start_165",
                    "dead": "dead_165"
                }
            },
            "Internal HR Reporting & Review": {
                "Prepare Monthly HR Activity Report": {
                    "start": "start_166",
                    "dead": "dead_166"
                },
                "Collect Department HR Updates": {
                    "start": "start_167",
                    "dead": "dead_167"
                },
                "Summarize HR Activities": {
                    "start": "start_168",
                    "dead": "dead_168"
                },
                "Prepare Quarterly HR Performance Report": {
                    "start": "start_169",
                    "dead": "dead_169"
                },
                "Analyze HR Process Efficiency": {
                    "start": "start_170",
                    "dead": "dead_170"
                },
                "Identify HR Improvement Areas": {
                    "start": "start_171",
                    "dead": "dead_171"
                },
                "Prepare HR Improvement Proposals": {
                    "start": "start_172",
                    "dead": "dead_172"
                },
                "Review HR Tool Usage": {
                    "start": "start_173",
                    "dead": "dead_173"
                },
                "Analyze HR System Data": {
                    "start": "start_174",
                    "dead": "dead_174"
                },
                "Prepare HR Digitalization Report": {
                    "start": "start_175",
                    "dead": "dead_175"
                },
                "Collect HR Feedback from Employees": {
                    "start": "start_176",
                    "dead": "dead_176"
                },
                "Analyze Employee Satisfaction": {
                    "start": "start_177",
                    "dead": "dead_177"
                },
                "Prepare Employee Feedback Summary": {
                    "start": "start_178",
                    "dead": "dead_178"
                },
                "Review HR Communication Effectiveness": {
                    "start": "start_179",
                    "dead": "dead_179"
                },
                "Prepare HR Communication Plan": {
                    "start": "start_180",
                    "dead": "dead_180"
                },
                "Update Internal HR Guidelines": {
                    "start": "start_181",
                    "dead": "dead_181"
                },
                "Prepare HR Knowledge Base Updates": {
                    "start": "start_182",
                    "dead": "dead_182"
                },
                "Validate HR Documentation Consistency": {
                    "start": "start_183",
                    "dead": "dead_183"
                },
                "Prepare HR Risk Assessment": {
                    "start": "start_184",
                    "dead": "dead_184"
                },
                "Review HR Compliance Status": {
                    "start": "start_185",
                    "dead": "dead_185"
                },
                "Prepare Annual HR Review": {
                    "start": "start_186",
                    "dead": "dead_186"
                },
                "Collect Leadership Feedback": {
                    "start": "start_187",
                    "dead": "dead_187"
                },
                "Revise HR Review Report": {
                    "start": "start_188",
                    "dead": "dead_188"
                },
                "Finalize HR Review Documentation": {
                    "start": "start_189",
                    "dead": "dead_189"
                },
                "Present HR Review to Management": {
                    "start": "start_190",
                    "dead": "dead_190"
                },
                "Document Management Decisions": {
                    "start": "start_191",
                    "dead": "dead_191"
                },
                "Update HR Action Plan": {
                    "start": "start_192",
                    "dead": "dead_192"
                },
                "Track HR Action Items": {
                    "start": "start_193",
                    "dead": "dead_193"
                },
                "Verify Action Item Completion": {
                    "start": "start_194",
                    "dead": "dead_194"
                },
                "Prepare HR Closure Report": {
                    "start": "start_195",
                    "dead": "dead_195"
                }
            }
        }
    }
}

SQL_REFRESH = """
USE task_management;
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE `report`;
TRUNCATE TABLE `task_for_users`;
TRUNCATE TABLE `task`;
TRUNCATE TABLE `collection`;
TRUNCATE TABLE `phase`;
TRUNCATE TABLE `project_role`;
TRUNCATE TABLE `project`;
SET FOREIGN_KEY_CHECKS = 1;
"""


def SQL_PROJ(
        proj_id,
        proj_name,
        created_t,
        due_d,
        start_d,
        creator
):
    return f"""
INSERT INTO project (`id`, `created_time`, `description`, `due_date`, `expected_start_date`, `name`, `status`, `updated_time`, `created_by_id`)
VALUES ({proj_id}, '{created_t}', 'This is {proj_name}', '{due_d}', '{start_d}', '{proj_name}', 'IN_PROGRESS', '{created_t}', {creator});
"""


def SQL_PROJ_ROLE(owner, o_id, member, m_id, proj_id):
    return f"""
INSERT INTO project_role (`id`, `role`, `project_id`, `user_info_id`) VALUES ({o_id}, 'OWNER', {proj_id}, {owner});
INSERT INTO project_role (`id`, `role`, `project_id`, `user_info_id`) VALUES ({m_id}, 'MEMBER', {proj_id}, {member});
"""


def SQL_PHASE(
        phase_id,
        proj_id,
        phase_name,
        created_t,
        due_d,
        start_d,
        creator
):
    return f"""
INSERT INTO `phase` (`id`, `created_time`, `description`, `due_date`, `start_date`, `name`, `updated_time`, `project_id`, `created_by_id`)
VALUES ({phase_id}, '{created_t}', 'This is {phase_name}', '{due_d}', '{start_d}', '{phase_name}', '{created_t}', {proj_id}, {creator});
"""


def SQL_COL(
        col_id,
        phase_id,
        col_name,
        created_t,
        due_d,
        start_d,
        creator
):
    return f"""
INSERT INTO collection (`id`, `created_time`, `description`, `due_date`, `start_date`, `name`, `updated_time`, `phase_id`, `created_by_id`)
VALUES ({col_id}, '{created_t}', 'This is {col_name}', '{due_d}', '{start_d}', '{col_name}', '{created_t}', {phase_id}, {creator});
"""


def SQL_TASK(
        task_id,
        col_id,
        task_name,
        created_t,
        dead_d,
        start_d,
        end_d,
        creator,
        level,
        ttype,
        priority
):
    return f"""
-- {created_t}
-- {start_d}
INSERT INTO task (id, collection_id, created_by_id, root_task_id, name, description, report_format, level, task_type, priority, is_locked, start_date, end_date, deadline, created_time, updated_time)
VALUES ({task_id}, {col_id}, {creator}, NULL, '{task_name}', 'This is {task_name}', NULL, '{level}', '{ttype}', '{priority}', FALSE, '{start_d}', '{end_d}', '{dead_d}', '{created_t}', '{created_t}');
"""


def SQL_TFU(
        TFU_ID: int,
        tfus: list,
        task_id,
        task_create_at,
):
    result_sql = "INSERT INTO task_for_users (id, task_id, assigned_to_id, user_task_status, updated_time, started_time)\nVALUES"
    for tfu in tfus:
        result_sql += f"\n({TFU_ID}, {task_id}, {tfu['user_id']}, 'JOINED', '{task_create_at}', '{tfu['start']}'),"
        TFU_ID += 1
    return result_sql[:-1] + ";", TFU_ID


def SQL_REPORT(TFU_ID: int, tfus: list):
    result_sql = f"INSERT INTO report (id, created_by_id, title, content, rejected_reason, report_status, created_time, updated_time, reviewed_time)\nVALUES"
    for tfu in tfus:
        result_sql += f"\n(DEFAULT, {TFU_ID}, 'Employee {tfu['user_id']} submit Report', 'Completed Task.', NULL, 'APPROVED', '{tfu['r_create']}', '{tfu['r_update']}', '{tfu['r_review']}'),"
        TFU_ID += 1
    return result_sql[:-1] + ";"
