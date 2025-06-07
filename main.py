from Gologin_API import create_profileQ, start_profileQ,stop_profileQ,Proxcy_setup
from linkedin_login import login_to_linkedinQ


def main():
    print("[*] Creating GoLogin profile...")
    profile_id = create_profileQ()

    print("[*] Seting Proxcy on profile...")
    profile_id = Proxcy_setup(profile_id)

    print("[*] Starting GoLogin profile...")
    debugger_address = start_profileQ(profile_id)
 
    print("[*] Launching Selenium browser...")
    driver = login_to_linkedinQ(debugger_address)

    input("[*] Press Enter to close browser and stop profile...")
    if driver is not None:
            driver.quit()
    stop_profileQ(profile_id)

if __name__ == "__main__":
    main()
