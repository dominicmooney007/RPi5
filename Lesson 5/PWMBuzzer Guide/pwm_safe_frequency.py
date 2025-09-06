#!/usr/bin/env python3
"""
Safe Frequency Playing with Error Handling
Demonstrates proper bounds checking and error handling for PWMOutputDevice
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
buzzer = PWMOutputDevice(22)

def safe_play_frequency(frequency, duration=1.0, volume=0.5):
    """
    Play frequency with bounds checking and error handling
    Most buzzers work between 100Hz and 10kHz
    """
    MIN_FREQ = 100
    MAX_FREQ = 10000
    
    try:
        # Validate frequency
        if not isinstance(frequency, (int, float)):
            raise TypeError(f"Frequency must be a number, got {type(frequency)}")
        
        if frequency < MIN_FREQ or frequency > MAX_FREQ:
            print(f"Warning: Frequency {frequency}Hz out of range ({MIN_FREQ}-{MAX_FREQ}Hz)")
            # Clamp to valid range
            frequency = max(MIN_FREQ, min(MAX_FREQ, frequency))
            print(f"Adjusted to: {frequency}Hz")
        
        # Validate volume
        if not 0 <= volume <= 1:
            print(f"Warning: Volume {volume} out of range (0.0-1.0)")
            volume = max(0, min(1, volume))
            print(f"Adjusted to: {volume}")
        
        # Validate duration
        if duration <= 0:
            raise ValueError(f"Duration must be positive, got {duration}")
        
        # Play the frequency
        print(f"Playing: {frequency}Hz at {int(volume*100)}% volume for {duration}s")
        buzzer.frequency = frequency
        buzzer.value = volume
        sleep(duration)
        buzzer.off()
        
        return True
        
    except TypeError as e:
        print(f"Type Error: {e}")
        buzzer.off()
        return False
        
    except ValueError as e:
        print(f"Value Error: {e}")
        buzzer.off()
        return False
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        buzzer.off()
        return False

def test_frequency_range():
    """Test the buzzer's frequency response"""
    print("Testing buzzer frequency range...")
    print("This will help identify your buzzer's effective range")
    print("-" * 50)
    
    test_frequencies = [
        50,    # Below typical range
        100,   # Minimum typical
        200,   # Low
        500,   # Mid-low
        1000,  # Middle (1kHz)
        2000,  # Mid-high
        5000,  # High
        10000, # Maximum typical
        15000, # Above typical range
    ]
    
    for freq in test_frequencies:
        print(f"\nTesting {freq}Hz:")
        safe_play_frequency(freq, duration=0.5, volume=0.5)
        sleep(0.5)
    
    print("\n" + "-" * 50)
    print("Frequency range test complete!")
    print("Note: If you didn't hear certain frequencies,")
    print("your buzzer may not support that range.")

def test_volume_levels():
    """Test different volume levels"""
    print("\nTesting volume levels at 1000Hz...")
    print("-" * 50)
    
    volumes = [0.1, 0.25, 0.5, 0.75, 1.0]
    
    for vol in volumes:
        percentage = int(vol * 100)
        print(f"\nVolume: {percentage}%")
        safe_play_frequency(1000, duration=0.5, volume=vol)
        sleep(0.3)
    
    print("\n" + "-" * 50)
    print("Volume test complete!")

def test_error_handling():
    """Test error handling with invalid inputs"""
    print("\nTesting error handling...")
    print("-" * 50)
    
    # Test invalid frequency types
    print("\n1. Testing invalid frequency type (string):")
    safe_play_frequency("not_a_number", duration=0.5)
    
    # Test out of range frequencies
    print("\n2. Testing frequency too low (10Hz):")
    safe_play_frequency(10, duration=0.5)
    
    print("\n3. Testing frequency too high (20000Hz):")
    safe_play_frequency(20000, duration=0.5)
    
    # Test invalid volume
    print("\n4. Testing invalid volume (1.5):")
    safe_play_frequency(1000, duration=0.5, volume=1.5)
    
    print("\n5. Testing negative volume (-0.5):")
    safe_play_frequency(1000, duration=0.5, volume=-0.5)
    
    # Test invalid duration
    print("\n6. Testing invalid duration (-1):")
    safe_play_frequency(1000, duration=-1)
    
    print("\n" + "-" * 50)
    print("Error handling test complete!")

def interactive_frequency_player():
    """Interactive mode for testing specific frequencies"""
    print("\n" + "=" * 50)
    print("Interactive Frequency Player")
    print("=" * 50)
    print("Enter frequency (Hz), volume (0-1), duration (seconds)")
    print("Format: frequency,volume,duration")
    print("Example: 440,0.5,1")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nEnter values (or 'quit'): ")
            
            if user_input.lower() == 'quit':
                break
            
            # Parse input
            parts = user_input.split(',')
            
            if len(parts) == 1:
                # Just frequency
                freq = float(parts[0])
                safe_play_frequency(freq)
            elif len(parts) == 2:
                # Frequency and volume
                freq = float(parts[0])
                vol = float(parts[1])
                safe_play_frequency(freq, volume=vol)
            elif len(parts) == 3:
                # All three parameters
                freq = float(parts[0])
                vol = float(parts[1])
                dur = float(parts[2])
                safe_play_frequency(freq, duration=dur, volume=vol)
            else:
                print("Invalid format. Use: frequency,volume,duration")
                
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

# Main demonstration
if __name__ == "__main__":
    print("Safe Frequency Playing Demonstration")
    print("=" * 50)
    
    # Run tests
    print("\n[Test 1: Frequency Range]")
    test_frequency_range()
    sleep(1)
    
    print("\n[Test 2: Volume Levels]")
    test_volume_levels()
    sleep(1)
    
    print("\n[Test 3: Error Handling]")
    test_error_handling()
    sleep(1)
    
    print("\n[Test 4: Interactive Mode]")
    interactive_frequency_player()
    
    print("\nAll tests complete!")
    buzzer.off()
