"""
BOT SIMULATOR - KEEPS BROWSER OPEN
Shows result before closing
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

print("="*80)
print("BOT SIMULATOR - SHOWS RESULTS")
print("="*80)

FRONTEND_URL = "http://localhost:5000/static/demo.html"

class BotSimulator:
    """Bot simulator that waits to show results"""
    
    def __init__(self, headless=False):
        from selenium.webdriver.chrome.options import Options
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        print("📥 Setting up ChromeDriver...")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.set_window_size(1400, 900)
        
        print("✅ Browser ready")
    
    def open_page(self):
        print(f"\n📱 Opening: {FRONTEND_URL}")
        self.driver.get(FRONTEND_URL)
        time.sleep(3)
        print("✅ Page loaded")
    
    def click_start_button(self):
        try:
            start_btn = self.driver.find_element(By.ID, "btnStart")
            start_btn.click()
            print("▶ Started tracking")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️  Could not click start: {e}")
    
    def get_tracking_area_size(self):
        try:
            tracking_area = self.driver.find_element(By.ID, "trackingArea")
            size = tracking_area.size
            width = int(size['width'] * 0.8)
            height = int(size['height'] * 0.8)
            print(f"📏 Tracking area: {width} x {height}")
            return width, height
        except:
            return 400, 300
    
    def speed_clicker_bot(self, duration=10):
        """Bot Type 1: Speed Clicker"""
        print(f"\n🤖 Running: SPEED CLICKER BOT ({duration}s)")
        
        buttons = self.driver.find_elements(By.CLASS_NAME, "click-button")
        
        end_time = time.time() + duration
        click_count = 0
        
        while time.time() < end_time:
            for button in buttons:
                if time.time() >= end_time:
                    break
                try:
                    button.click()
                    click_count += 1
                    time.sleep(0.08)  # 12.5 clicks/sec
                except:
                    pass
        
        print(f"✅ Completed: {click_count} clicks")
        print(f"   Rate: {click_count/duration:.1f} clicks/sec")
    
    def linear_mover_bot(self, duration=10):
        """Bot Type 2: Linear Mover"""
        print(f"\n🤖 Running: LINEAR MOVER BOT ({duration}s)")
        
        tracking_area = self.driver.find_element(By.ID, "trackingArea")
        width, height = self.get_tracking_area_size()
        
        margin = 20
        min_x, max_x = margin, width - margin
        min_y, max_y = margin, height - margin
        
        end_time = time.time() + duration
        move_count = 0
        
        while time.time() < end_time:
            # Horizontal sweep
            y = random.randint(min_y, max_y)
            
            for x in range(min_x, max_x, 15):
                if time.time() >= end_time:
                    break
                try:
                    self.driver.execute_script("""
                        var elem = arguments[0];
                        var event = new MouseEvent('mousemove', {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: elem.getBoundingClientRect().left + arguments[1],
                            clientY: elem.getBoundingClientRect().top + arguments[2]
                        });
                        elem.dispatchEvent(event);
                    """, tracking_area, x, y)
                    time.sleep(0.01)
                    move_count += 1
                except:
                    break
            
            # Vertical sweep
            x = random.randint(min_x, max_x)
            
            for y in range(min_y, max_y, 15):
                if time.time() >= end_time:
                    break
                try:
                    self.driver.execute_script("""
                        var elem = arguments[0];
                        var event = new MouseEvent('mousemove', {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: elem.getBoundingClientRect().left + arguments[1],
                            clientY: elem.getBoundingClientRect().top + arguments[2]
                        });
                        elem.dispatchEvent(event);
                    """, tracking_area, x, y)
                    time.sleep(0.01)
                    move_count += 1
                except:
                    break
        
        print(f"✅ Completed: {move_count} linear movements")
    
    def pattern_scanner_bot(self, duration=10):
        """Bot Type 3: Pattern Scanner"""
        print(f"\n🤖 Running: PATTERN SCANNER BOT ({duration}s)")
        
        tracking_area = self.driver.find_element(By.ID, "trackingArea")
        width, height = self.get_tracking_area_size()
        
        margin = 30
        step = 50
        
        end_time = time.time() + duration
        scan_count = 0
        
        while time.time() < end_time:
            for y in range(margin, height - margin, step):
                for x in range(margin, width - margin, step):
                    if time.time() >= end_time:
                        break
                    try:
                        self.driver.execute_script("""
                            var elem = arguments[0];
                            var event = new MouseEvent('mousemove', {
                                view: window,
                                bubbles: true,
                                cancelable: true,
                                clientX: elem.getBoundingClientRect().left + arguments[1],
                                clientY: elem.getBoundingClientRect().top + arguments[2]
                            });
                            elem.dispatchEvent(event);
                        """, tracking_area, x, y)
                        time.sleep(0.05)
                        scan_count += 1
                    except:
                        pass
        
        print(f"✅ Completed: {scan_count} grid points")
    
    def aggressive_scraper_bot(self, duration=10):
        """Bot Type 4: Aggressive Scraper"""
        print(f"\n🤖 Running: AGGRESSIVE SCRAPER BOT ({duration}s)")
        
        tracking_area = self.driver.find_element(By.ID, "trackingArea")
        buttons = self.driver.find_elements(By.CLASS_NAME, "click-button")
        width, height = self.get_tracking_area_size()
        
        end_time = time.time() + duration
        action_count = 0
        
        while time.time() < end_time:
            # Ultra-fast clicking
            for button in buttons:
                if time.time() >= end_time:
                    break
                try:
                    button.click()
                    action_count += 1
                    time.sleep(0.05)
                except:
                    pass
            
            # Fast movements
            for _ in range(5):
                if time.time() >= end_time:
                    break
                try:
                    x = random.randint(50, width - 50)
                    y = random.randint(50, height - 50)
                    self.driver.execute_script("""
                        var elem = arguments[0];
                        var event = new MouseEvent('mousemove', {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: elem.getBoundingClientRect().left + arguments[1],
                            clientY: elem.getBoundingClientRect().top + arguments[2]
                        });
                        elem.dispatchEvent(event);
                    """, tracking_area, x, y)
                    time.sleep(0.01)
                except:
                    pass
        
        print(f"✅ Completed: {action_count} actions")
    
    def wait_for_result(self, wait_time=5):
        """Wait and show the detection result"""
        print(f"\n⏳ Waiting {wait_time} seconds for detection result...")
        time.sleep(wait_time)
        
        try:
            # Try to get the result from the page
            result_elem = self.driver.find_element(By.ID, "predictionDisplay")
            result_text = result_elem.text
            
            print(f"\n{'='*60}")
            print(f"🎯 DETECTION RESULT")
            print(f"{'='*60}")
            print(f"  {result_text}")
            
            # Try to get probability
            try:
                prob_elem = self.driver.find_element(By.ID, "confidenceText")
                prob_text = prob_elem.text
                print(f"  Bot Probability: {prob_text}")
            except:
                pass
            
            # Try to get model info
            try:
                model_elem = self.driver.find_element(By.ID, "selectedModel")
                model_text = model_elem.text
                print(f"  Model Used: {model_text}")
            except:
                pass
            
            print(f"{'='*60}")
            
        except Exception as e:
            print(f"⚠️  Could not read result: {e}")
    
    def close(self, keep_open=False, wait_before_close=10):
        """Close browser with option to keep it open"""
        if keep_open:
            print(f"\n🌐 Browser will stay open for {wait_before_close} seconds")
            print(f"   Check the frontend to see the result!")
            print(f"   Press Ctrl+C to close early...")
            
            try:
                time.sleep(wait_before_close)
            except KeyboardInterrupt:
                print("\n⚠️  Closing browser...")
        
        print("\n🔒 Closing browser...")
        self.driver.quit()
        print("✅ Browser closed")

class HumanSimulator(BotSimulator):
    """Simulates realistic human behavior"""
    
    def natural_human_behavior(self, duration=15):
        """Natural human with curves and pauses"""
        print(f"\n👤 Running: NATURAL HUMAN BEHAVIOR ({duration}s)")
        
        tracking_area = self.driver.find_element(By.ID, "trackingArea")
        buttons = self.driver.find_elements(By.CLASS_NAME, "click-button")
        width, height = self.get_tracking_area_size()
        
        margin = 50
        
        end_time = time.time() + duration
        move_count = 0
        
        while time.time() < end_time:
            # Curved movement
            start_x = random.randint(margin, width - margin)
            start_y = random.randint(margin, height - margin)
            end_x = random.randint(margin, width - margin)
            end_y = random.randint(margin, height - margin)
            
            # Create curve
            points = []
            for i in range(5):
                t = i / 4.0
                x = int(start_x + (end_x - start_x) * t + random.randint(-30, 30))
                y = int(start_y + (end_y - start_y) * t + random.randint(-30, 30))
                x = max(margin, min(width - margin, x))
                y = max(margin, min(height - margin, y))
                points.append((x, y))
            
            # Move slowly along curve
            for x, y in points:
                if time.time() >= end_time:
                    break
                try:
                    self.driver.execute_script("""
                        var elem = arguments[0];
                        var event = new MouseEvent('mousemove', {
                            view: window,
                            bubbles: true,
                            cancelable: true,
                            clientX: elem.getBoundingClientRect().left + arguments[1],
                            clientY: elem.getBoundingClientRect().top + arguments[2]
                        });
                        elem.dispatchEvent(event);
                    """, tracking_area, x, y)
                    time.sleep(random.uniform(0.15, 0.35))
                    move_count += 1
                except:
                    pass
            
            # Human pause
            if random.random() < 0.4:
                time.sleep(random.uniform(1.0, 2.5))
            
            # Slow click
            if random.random() < 0.15:
                try:
                    random.choice(buttons).click()
                    time.sleep(random.uniform(0.6, 1.5))
                except:
                    pass
        
        print(f"✅ Natural human: {move_count} movements")

def run_demo():
    print("\n" + "="*80)
    print("BOT TYPES:")
    print("="*80)
    print("  1. Speed Clicker (12 clicks/sec)")
    print("  2. Linear Mover (straight lines)")
    print("  3. Pattern Scanner (grid)")
    print("  4. Aggressive Scraper (very fast)")
    print("  5. Human Simulator (curves + pauses)")
    print("="*80)
    
    choice = input("\nSelect (1-5): ").strip()
    
    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("❌ Invalid")
        return
    
    choice = int(choice)
    
    duration = input("Duration (default 10): ").strip()
    duration = int(duration) if duration.isdigit() else 10
    
    # NEW: Ask how long to keep browser open
    keep_open_time = input("Keep browser open after test (seconds, default 15): ").strip()
    keep_open_time = int(keep_open_time) if keep_open_time.isdigit() else 15
    
    headless = input("Headless? (y/n, default n): ").strip().lower() == 'y'
    
    print("\n" + "="*80)
    print("STARTING SIMULATION")
    print("="*80)
    
    simulator = HumanSimulator(headless) if choice == 5 else BotSimulator(headless)
    
    simulator.open_page()
    simulator.click_start_button()
    
    if choice == 1:
        simulator.speed_clicker_bot(duration)
    elif choice == 2:
        simulator.linear_mover_bot(duration)
    elif choice == 3:
        simulator.pattern_scanner_bot(duration)
    elif choice == 4:
        simulator.aggressive_scraper_bot(duration)
    elif choice == 5:
        simulator.natural_human_behavior(duration)
    
    # NEW: Wait for result and show it
    simulator.wait_for_result(wait_time=5)
    
    # NEW: Keep browser open so you can see the result
    simulator.close(keep_open=True, wait_before_close=keep_open_time)
    
    print("\n" + "="*80)
    print("✅ SIMULATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\n⚠️  Stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()