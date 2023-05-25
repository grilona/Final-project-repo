import simplejson as json
import csv


def check_string_in_document(data, search_string):

    if search_string in json.dumps(data):
        return 1
    else:
        return 0


def extract():
    with open("./MrsMajor3.0-TROJ.json") as f:
        data = json.load(f)

    with open("./malclass.csv", mode="a") as f:
        writer = csv.writer(f)
        score = (data['info']['score'])
        recon_fingerprint = (check_string_in_document(data, "recon_fingerprint"))
        pe_features = (check_string_in_document(data, "pe_features"))
        js_eval = (check_string_in_document(data, "js_eval"))
        creates_exe = (check_string_in_document(data, "creates_exe"))
        exe_appdata = (check_string_in_document(data, "exe_appdata"))
        stealth_window = (check_string_in_document(data, "stealth_window"))
        deletes_executed_files = (check_string_in_document(data, "deletes_executed_files"))
        dropper = (check_string_in_document(data, "dropper"))
        modify_uac_prompt = (check_string_in_document(data, "mmodify_uac_prompt"))
        process_martian = (check_string_in_document(data, "process_martian"))
        injection_resumethread = (check_string_in_document(data, "injection_resumethread"))
        suspicious_write_exe = (check_string_in_document(data, "suspicious_write_exe"))
        antivm_queries_computername = (check_string_in_document(data, "antivm_queries_computername"))
        console_output = (check_string_in_document(data, "console_output"))
        antivm_memory_available = (check_string_in_document(data, "antivm_memory_available"))
        raises_exception = (check_string_in_document(data, "raises_exception"))
        dumped_buffer = (check_string_in_document(data, "dumped_buffer"))
        p2p_cnc = (check_string_in_document(data, "p2p_cnc"))
        allocates_rwx = (check_string_in_document(data, "allocates_rwx"))
        antivm_disk_size = (check_string_in_document(data, "antivm_disk_size"))
        creates_doc = (check_string_in_document(data, "creates_doc"))
        suspicious_process = (check_string_in_document(data, "suspicious_process"))
        has_wmi = (check_string_in_document(data, "has_wmi"))
        moves_self = (check_string_in_document(data, "moves_self"))
        antivm_network_adapters=(check_string_in_document(data,"antivm_network_adapters"))
        privilege_luid_check = (check_string_in_document(data,"privilege_luid_check"))
        terminates_remote_process = (check_string_in_document(data,"terminates_remote_process"))
        uses_windows_utilities = (check_string_in_document(data,"uses_windows_utilities"))
        nolookup_communication = (check_string_in_document(data,"nolookup_communication"))
        bypass_firewall = (check_string_in_document(data, "bypass_firewall"))
        antisandbox_cuckoo_files = (check_string_in_document(data, "antisandbox_cuckoo_files"))
        disables_proxy =(check_string_in_document(data, "disables_proxy"))
        modifies_proxy_wpad = (check_string_in_document(data, "modifies_proxy_wpad"))
        ransomware_message = (check_string_in_document(data, "ransomware_message"))
        protection_rx = (check_string_in_document(data, "protection_rx"))
        persistence_autorun = (check_string_in_document(data, "persistence_autorun"))
        peid_packer = (check_string_in_document(data, "peid_packer"))
        antisandbox_foregroundwindows = (check_string_in_document(data, "antisandbox_foregroundwindows"))
        creates_shortcut = (check_string_in_document(data, "creates_shortcut"))
        imported_dll_count = (data['static']['imported_dll_count'])
        tls = (len(data['network']['tls']))
        udp = (len(data['network']['udp']))
        dns_servers = (len(data['network']['dns_servers']))
        http = (len(data['network']['http']))
        irc = (len(data['network']['irc']))
        smtp = (len(data['network']['smtp']))
        tcp = (len(data['network']['tcp']))
        smtp_ex = (len(data['network']['smtp_ex']))
        mitm = (len(data['network']['mitm']))
        hosts = (len(data['network']['hosts']))
        dns = (len(data['network']['dns']))
        domains = (len(data['network']['domains']))
        dead_hosts = (len(data['network']['dead_hosts']))
        icmp = (len(data['network']['icmp']))
        http_ex = (len(data['network']['http_ex']))































        writer.writerow(["score","recon_fingerprint","pe_features", "js_eval","creates_exe","exe_appdata", "stealth_window",
                         "deletes_executed_files", "dropper",  "modify_uac_prompt", "process_martian", "injection_resumethread",
                         "suspicious_write_exe", "antivm_queries_computername","console_output", "antivm_memory_available",
                         "raises_exception", "dumped_buffer","p2p_cnc,allocates_rwx","antivm_disk_size","creates_doc",
                         "suspicious_process","has_wmi,moves_self","antivm_network_adapters","privilege_luid_check",
                         "terminates_remote_process","uses_windows_utilities", "nolookup_communication","bypass_firewall",
                         "antisandbox_cuckoo_files","disables_proxy","modifies_proxy_wpad","ransomware_message",
                          "protection_rx","persistence_autorun", "peid_packer","antisandbox_foregroundwindows","creates_shortcut",
                         "imported_dll_count","tls","udp", 'dns_servers', 'http', "irc", "smtp", 'tcp', "smtp_ex", 'mitm', "hosts", "dns",
                         "domains",'dead_hosts', 'icmp', 'http_ex'
                        ])
        writer.writerow([score,recon_fingerprint,pe_features, js_eval,creates_exe,exe_appdata, stealth_window,
                         deletes_executed_files, dropper,  modify_uac_prompt, process_martian, injection_resumethread,
                         suspicious_write_exe, antivm_queries_computername,console_output, antivm_memory_available,
                         raises_exception, dumped_buffer,p2p_cnc,allocates_rwx,antivm_disk_size,creates_doc,
                         suspicious_process,has_wmi,moves_self,antivm_network_adapters,privilege_luid_check,
                         terminates_remote_process,uses_windows_utilities, nolookup_communication,bypass_firewall,
                         antisandbox_cuckoo_files,disables_proxy,modifies_proxy_wpad,ransomware_message,
                          protection_rx,persistence_autorun, peid_packer,antisandbox_foregroundwindows,creates_shortcut,
                         imported_dll_count,tls,udp, dns_servers, http, irc, smtp, tcp, smtp_ex, mitm, hosts, dns,
                         domains,dead_hosts, icmp, http_ex
                         ])

    # Closing file
    f.close()
    print("CSV file saved successfully.")


extract()

