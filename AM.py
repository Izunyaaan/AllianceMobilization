import pyautogui
import time
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Locate Images
def locate_images(image_path):
    try:
        if pyautogui.locateOnScreen(image_path, confidence=0.95) is not None:
            time.sleep(0.69)
            locations = pyautogui.locateAllOnScreen(image_path, confidence=0.95)
            time.sleep(0.69)
            return list(locations)
    except Exception as e:
        # print(f"Error locating image: {e}")
        return None
    
# Read task description
def read_task_description():
    for task_description in LIST_OF_TASK_DESCRIPTIONS:
        try:
            location = pyautogui.locateOnScreen(task_description, confidence=0.8)
            time.sleep(0.69)
            if location is not None:
                x, y, width, height = location
                screenshot = pyautogui.screenshot(region=(int(x), int(y), int(width), int(height)))
                time.sleep(0.69)
                text = pytesseract.image_to_string(screenshot)
                return text
            
        except Exception as e:
            print(f"Error locating task image: {e}")
    return None

# Refresh a task
def refresh_task():
    try:
        refresh_mission_button = pyautogui.locateCenterOnScreen("UIElements/refresh_mission.png", confidence=0.96)
        pyautogui.click(refresh_mission_button)
        time.sleep(0.69)
        refresh_button = pyautogui.locateCenterOnScreen("UIElements/refresh.png", confidence=0.96)
        pyautogui.click(refresh_button)
        time.sleep(0.69)
    except Exception as e:
        print(f"Error refreshing task: {e}")

# Close a task
def close_task():
    try:
        close_button = pyautogui.locateCenterOnScreen("UIElements/close.png", confidence=0.96)
        time.sleep(0.69)
        pyautogui.click(close_button)
        time.sleep(0.69)
    except Exception as e:
        print(f"Error closing task: {e}. Retrying...")
        time.sleep(0.69)
        close_task()

LIST_OF_TASKS_TO_REFRESH = [
    "Tasks/Beasts.png",
    "Tasks/Charm.png",
    "Tasks/ChiefGear.png",
    # "Tasks/Construction.png",
    "Tasks/Gathering.png",
    "Tasks/GearEssence.png",
    "Tasks/Gems.png",
    "Tasks/General.png",
    "Tasks/Money.png",
    "Tasks/PolarTerror.png",
    "Tasks/Research.png",
    "Tasks/Shards.png",
    # "Tasks/Train_Troops.png",
    "Tasks/Training.png",
]

LIST_OF_TASKS_TO_CHECK = [
    # "Tasks/Beasts.png",
    # "Tasks/Charm.png",
    # "Tasks/ChiefGear.png",
    "Tasks/Construction.png",
    # "Tasks/Gathering.png",
    # "Tasks/GearEssence.png",
    # "Tasks/Gems.png",
    # "Tasks/General.png",
    # "Tasks/Money.png",
    # "Tasks/PolarTerror.png",
    # "Tasks/Research.png",
    # "Tasks/Shards.png",
    "Tasks/Train_Troops.png",
    # "Tasks/Training.png",
]

LIST_OF_TASK_DESCRIPTIONS = [
    'TaskDescriptions/TrainTroops.png',
    # 'TaskDescriptions/RaiseChiefGear.png',
    'TaskDescriptions/ConstructionSpeedup.png',
]

LIST_OF_DESCRIPTIONS_TO_REFRESH = [
    "Raise 15,000 Power",
    "Raise 30,000 Power",
    "Use 3,600m",
    # "Use 1,800m",

]

LIST_OF_DESCRIPTIONS_TO_KEEP = [
    # "Defeat Polar Terror",
    "Raise 120,000 Power",
    # "Use 7,200m",
    "Use 1,800m",
]

refresh_count = 0
loop_count = 0

print(f"Starting the task at {time.ctime()}. Press Ctrl+C to stop.")

while True:
    for task in LIST_OF_TASKS_TO_REFRESH:
        locations = locate_images(task)
        if locations:
            for location in locations:
                print(f"Found {task} at {location}")
                center = pyautogui.center(location)
                time.sleep(0.69)
                pyautogui.click(center)
                time.sleep(0.69)
                refresh_task()
                refresh_count += 1
            time.sleep(0.69)
        time.sleep(0.69)

    for task in LIST_OF_TASKS_TO_CHECK:
        locations = locate_images(task)
        if locations:
            for location in locations:
                print(f"Found {task} at {location}")
                center = pyautogui.center(location)
                time.sleep(0.69)
                pyautogui.click(center)
                time.sleep(0.69)
                task_description = read_task_description()
                if task_description:
                    # print(f"Task description: {task_description}")
                    for details in LIST_OF_DESCRIPTIONS_TO_REFRESH:
                        if task_description.find(details) != -1:
                            print(f"Refreshing task with description: {task_description}")
                            refresh_task()
                            refresh_count += 1
                            time.sleep(0.69)
                    for details in LIST_OF_DESCRIPTIONS_TO_KEEP:
                        if task_description.find(details) != -1:
                            print(f"Keeping task with description: {task_description}")
                            close_task()
                            time.sleep(0.69)
            time.sleep(0.69)

    loop_count += 1
    print(f"Loop {loop_count} completed. Total refreshes: {refresh_count}. Resting for 4.20 seconds.")
    time.sleep(4.20)