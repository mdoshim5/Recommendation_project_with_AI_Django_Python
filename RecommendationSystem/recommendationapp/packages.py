packages = [
    {
        "vcpu": 2,                                      #1. intel haswell
        "ram" : 2, #GB                                  #2. aws nitro
        "storage_type" : 3, #EBS                        #3. intel Xeon pentium
        "storage_amount" : 128, #GB
        "network_bandwidth" : 25, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 1
    },
    {
        "vcpu": 8,
        "ram" : 2, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 256, #GB
        "network_bandwidth" : 30, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 2
    },
    {
        "vcpu": 14,
        "ram" : 4, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 512, #GB
        "network_bandwidth" : 30, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 3
    },
    {
        "vcpu": 20,
        "ram" : 4, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 512, #GB
        "network_bandwidth" : 40, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 4
    },
    {
        "vcpu": 26,
        "ram" : 8, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 512, #GB
        "network_bandwidth" : 40, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 5
    },
    {
        "vcpu": 32,
        "ram" : 8, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 50, #Gbps
        "processor" : 3, # intel Xeon pentium
        "package": 6
    },
    {
        "vcpu": 38,
        "ram" : 16, #GB
        "storage_type" : 3, #EBS
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 50, #Gbps
        "processor" : 2, #aws nitro
        "package": 7
    },
    {
        "vcpu": 44,
        "ram" : 16, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : 2, #aws nitro
        "package": 8
    },
    {
        "vcpu": 50,
        "ram" : 32, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : 2, #aws nitro
        "package": 9
    },
    {
        "vcpu": 56,
        "ram" : 32, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : 2, #aws nitro
        "package": 10
    },
    {
        "vcpu": 62,
        "ram" : 64, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : 2, #aws nitro
        "package": 11
    },
    {
        "vcpu": 70,
        "ram" : 64, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : 2, #aws nitro
        "package": 12
    },
    {
        "vcpu": 78,
        "ram" : 128, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : 2, #aws nitro
        "package": 13
    },
    {
        "vcpu": 86,
        "ram" : 128, #GB
        "storage_type" : 2, #EBS
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : 2, #aws nitro
        "package": 14
    },
    {
        "vcpu": 96,
        "ram" : 256, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : 1, #intel haswell,
        "package": 15
    },
    {
        "vcpu": 102,
        "ram" : 256, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : 1, #intel haswell,
        "package": 16
    },
    {
        "vcpu": 110,
        "ram" : 512, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : 1, #intel haswell,
        "package": 17
    },
    {
        "vcpu": 116,
        "ram" : 512, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : 1, #intel haswell,
        "package": 18
    },
    {
        "vcpu": 122,
        "ram" : 1024, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : 1, #intel haswell,
        "package": 19
    },
    {
        "vcpu": 128,
        "ram" : 1024, #GB
        "storage_type" : 1, #EBS
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : 1, #intel haswell,
        "package": 20
    },
]

packages2 = [
    {
        "company_size": 2,
        "hits": 2,
        "package": 1
    },
    {
        "company_size": 2,
        "hits": 4,
        "package": 3
    },
    {
        "company_size": 2,
        "hits": 10,
        "package": 4
    },
    {
        "company_size": 2,
        "hits": 30,
        "package": 5
    },
    {
        "company_size": 5,
        "hits": 2,
        "package": 6
    },
     {
        "company_size": 5,
        "hits": 4,
        "package": 7
    },
    {
        "company_size": 5,
        "hits": 10,
        "package": 8
    },
    {
        "company_size": 5,
        "hits": 30,
        "package": 10
    },
    {
        "company_size": 10,
        "hits": 2,
        "package": 11
    },
    {
        "company_size": 10,
        "hits": 4,
        "package": 12
    },
     {
        "company_size": 10,
        "hits": 10,
        "package": 14
    },
    {
        "company_size": 10,
        "hits": 30,
        "package": 15
    },
    {
        "company_size": 20,
        "hits": 2,
        "package": 16
    },
    {
        "company_size": 20,
        "hits": 4,
        "package": 17
    },
    {
        "company_size": 20,
        "hits": 10,
        "package": 18
    },
     {
        "company_size": 20,
        "hits": 30,
        "package": 20
    },
]

packages_with_details = [
    {
        "vcpu": 2,                                      #1. intel haswell
        "ram" : 2, #GB                                  #2. aws nitro
        "storage_type" : "HDD",                         #3. intel Xeon pentium
        "storage_amount" : 128, #GB 
        "network_bandwidth" : 25, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 1
    },
    {
        "vcpu": 8,
        "ram" : 2, #GB
        "storage_type" : "HDD",
        "storage_amount" : 256, #GB
        "network_bandwidth" : 30, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 2
    },
    {
        "vcpu": 14,
        "ram" : 4, #GB
        "storage_type" : "HDD",
        "storage_amount" : 512, #GB
        "network_bandwidth" : 30, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 3
    },
    {
        "vcpu": 20,
        "ram" : 4, #GB
        "storage_type" : "HDD",
        "storage_amount" : 512, #GB
        "network_bandwidth" : 40, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 4
    },
    {
        "vcpu": 26,
        "ram" : 8, #GB
        "storage_type" : "HDD",
        "storage_amount" : 512, #GB
        "network_bandwidth" : 40, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 5
    },
    {
        "vcpu": 32,
        "ram" : 8, #GB
        "storage_type" : "HDD",
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 50, #Gbps
        "processor" : "Intel Xeon Pentium 8176M",
        "package": 6
    },
    {
        "vcpu": 38,
        "ram" : 16, #GB
        "storage_type" : "HDD",
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 50, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 7
    },
    {
        "vcpu": 44,
        "ram" : 16, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 1024, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 8
    },
    {
        "vcpu": 50,
        "ram" : 32, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 9
    },
    {
        "vcpu": 56,
        "ram" : 32, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 60, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 10
    },
    {
        "vcpu": 62,
        "ram" : 64, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 2048, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 11
    },
    {
        "vcpu": 70,
        "ram" : 64, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 12
    },
    {
        "vcpu": 78,
        "ram" : 128, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 70, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 13
    },
    {
        "vcpu": 86,
        "ram" : 128, #GB
        "storage_type" : "NVMe SSD",
        "storage_amount" : 3072, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : "AWS Nitro System Xeon",
        "package": 14
    },
    {
        "vcpu": 96,
        "ram" : 256, #GB
        "storage_type" : "EBS",
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 15
    },
    {
        "vcpu": 102,
        "ram" : 256, #GB
        "storage_type" : "EBS",
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 16
    },
    {
        "vcpu": 110,
        "ram" : 512, #GB
        "storage_type" : "EBS",
        "storage_amount" : 4096, #GB
        "network_bandwidth" : 80, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 17
    },
    {
        "vcpu": 116,
        "ram" : 512, #GB
        "storage_type" : "EBS",
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 18
    },
    {
        "vcpu": 122,
        "ram" : 1024, #GB
        "storage_type" : "EBS",
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 19
    },
    {
        "vcpu": 128,
        "ram" : 1024, #GB
        "storage_type" : "EBS",
        "storage_amount" : 5120, #GB
        "network_bandwidth" : 100, #Gbps
        "processor" : "Custom Intel Xeon E5-2076 V3 Haswell",
        "package": 20
    },
]
