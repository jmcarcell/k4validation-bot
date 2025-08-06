import ROOT
import numpy as np

# Generate normally distributed random samples
# Using numpy for easier random generation
np.random.seed(42)  # For reproducibility
sample1_norm = np.random.normal(2.5, 1.0, 1000)  # mean=2.5, std=1.0, 1000 points
sample2_norm = np.random.normal(2.0, 1.2, 1000)  # mean=2.0, std=1.2, 1000 points

# Generate exponentially distributed random samples
# Using different seeds to get different distributions
np.random.seed(123)
sample1_exp = np.random.exponential(3.0, 1000)  # scale=3.0, 1000 points
np.random.seed(456)
sample2_exp = np.random.exponential(4.0, 1000)  # scale=4.0, 1000 points

# Create first ROOT file with both histograms
output_file1 = ROOT.TFile("hist1.root", "RECREATE")

# Normal distribution histogram
hist1_norm = ROOT.TH1F("norm", "Normal Distribution;Value;Counts", 50, 0, 5)
for value in sample1_norm:
    if 0 <= value <= 5:  # Only fill values within range
        hist1_norm.Fill(value)

hist1_norm.SetLineColor(ROOT.kBlue)
hist1_norm.SetFillColor(ROOT.kBlue)
hist1_norm.SetFillStyle(3004)  # Hatched pattern

# Exponential distribution histogram
hist1_exp = ROOT.TH1F("exp", "Exponential Distribution;Value;Counts", 50, 0, 25)
for value in sample1_exp:
    if 0 <= value <= 25:  # Only fill values within range
        hist1_exp.Fill(value)

hist1_exp.SetLineColor(ROOT.kGreen)
hist1_exp.SetFillColor(ROOT.kGreen)
hist1_exp.SetFillStyle(3006)  # Different hatched pattern

# Write and close first file
hist1_norm.Write()
hist1_exp.Write()
entries1_norm = hist1_norm.GetEntries()
entries1_exp = hist1_exp.GetEntries()
output_file1.Close()

# Create second ROOT file with both histograms
output_file2 = ROOT.TFile("hist2.root", "RECREATE")

# Normal distribution histogram
hist2_norm = ROOT.TH1F("norm", "Normal Distribution;Value;Counts", 50, 0, 5)
for value in sample2_norm:
    if 0 <= value <= 5:  # Only fill values within range
        hist2_norm.Fill(value)

hist2_norm.SetLineColor(ROOT.kRed)
hist2_norm.SetFillColor(ROOT.kRed)
hist2_norm.SetFillStyle(3005)  # Different hatched pattern

# Exponential distribution histogram
hist2_exp = ROOT.TH1F("exp", "Exponential Distribution;Value;Counts", 50, 0, 25)
for value in sample2_exp:
    if 0 <= value <= 25:  # Only fill values within range
        hist2_exp.Fill(value)

hist2_exp.SetLineColor(ROOT.kMagenta)
hist2_exp.SetFillColor(ROOT.kMagenta)
hist2_exp.SetFillStyle(3007)  # Different hatched pattern

# Write and close second file
hist2_norm.Write()
hist2_exp.Write()
entries2_norm = hist2_norm.GetEntries()
entries2_exp = hist2_exp.GetEntries()
output_file2.Close()

# For plotting, we need to reopen the files
file1 = ROOT.TFile("hist1.root", "READ")
file2 = ROOT.TFile("hist2.root", "READ")
hist1_norm_plot = file1.Get("norm")
hist1_exp_plot = file1.Get("exp")
hist2_norm_plot = file2.Get("norm")
hist2_exp_plot = file2.Get("exp")

# Create canvas for normal distributions
canvas1 = ROOT.TCanvas("canvas1", "Normal Distributions Comparison", 800, 600)
hist1_norm_plot.Draw("HIST")
hist2_norm_plot.Draw("HIST SAME")

legend1 = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend1.AddEntry(hist1_norm_plot, "File1: Mean=2.5, Std=1.0", "f")
legend1.AddEntry(hist2_norm_plot, "File2: Mean=2.0, Std=1.2", "f")
legend1.Draw()
canvas1.Update()

# Create canvas for exponential distributions
canvas2 = ROOT.TCanvas("canvas2", "Exponential Distributions Comparison", 800, 600)
hist1_exp_plot.Draw("HIST")
hist2_exp_plot.Draw("HIST SAME")

legend2 = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend2.AddEntry(hist1_exp_plot, "File1: Scale=3.0", "f")
legend2.AddEntry(hist2_exp_plot, "File2: Scale=4.0", "f")
legend2.Draw()
canvas2.Update()

print("Created hist1.root and hist2.root with normal and exponential distribution histograms")
print(f"File 1 - Normal histogram: {entries1_norm} entries")
print(f"File 1 - Exponential histogram: {entries1_exp} entries")
print(f"File 2 - Normal histogram: {entries2_norm} entries")
print(f"File 2 - Exponential histogram: {entries2_exp} entries")

# Keep the window open - wait for user input
input("Press Enter to close the plots and exit...")

# Close the read files
file1.Close()
file2.Close()