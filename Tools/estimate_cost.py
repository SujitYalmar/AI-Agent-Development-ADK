#!/usr/bin/env python3
"""Gemini API Cost Estimator

This script provides rough cost estimates for Google Gemini API usage.
For accurate billing information, always check the Google Cloud Console.

Note: Prices are approximate and may change. Verify current pricing at:
https://ai.google.dev/pricing
"""

def print_pricing_table():
    print("=" * 70)
    print("Google Gemini API - Approximate Pricing (as of November 2025)")
    print("=" * 70)
    print()
    
    print("Model: gemini-1.5-flash")
    print("-" * 70)
    print("  Input:  Free for first 15 requests/min, 1M requests/day")
    print("  Output: Free for first 15 requests/min, 1M requests/day")
    print("  Notes:  Best for learning and course work")
    print("          Often completely free for typical usage")
    print()
    
    print("Model: gemini-1.5-pro")
    print("-" * 70)
    print("  Input:  ~$0.00125 per 1K characters (~$0.0025 per 1K tokens)")
    print("  Output: ~$0.00500 per 1K characters (~$0.0100 per 1K tokens)")
    print("  Notes:  More powerful but costs more")
    print("          Use when flash model is insufficient")
    print()
    
    print("=" * 70)
    print("IMPORTANT: These are rough estimates only!")
    print("Check your actual usage and billing at:")
    print("https://console.cloud.google.com/")
    print("=" * 70)
    print()

def estimate_cost(model, input_chars, output_chars):
    """Estimate cost for a single request."""
    if model == "flash":
        return 0.0
    elif model == "pro":
        input_cost = (input_chars / 1000) * 0.00125
        output_cost = (output_chars / 1000) * 0.00500
        return input_cost + output_cost
    else:
        return 0.0

def main():
    print()
    print_pricing_table()
    print("Example Calculations:")
    print("-" * 70)
    print("Example 1: 500 char prompt, 200 char response (flash)")
    cost = estimate_cost("flash", 500, 200)
    print(f"  Estimated cost: ${cost:.4f}")
    print()
    print("Example 2: 2000 char prompt, 1000 char response (pro)")
    cost = estimate_cost("pro", 2000, 1000)
    print(f"  Estimated cost: ${cost:.4f}")
    print()
    print("Example 3: 10000 char prompt, 500 char response (pro)")
    cost = estimate_cost("pro", 10000, 500)
    print(f"  Estimated cost: ${cost:.4f}")
    print()
    print("-" * 70)
    print("Recommendation: Use gemini-1.5-flash for the course to minimize costs.")
    print()

if __name__ == "__main__":
    main()