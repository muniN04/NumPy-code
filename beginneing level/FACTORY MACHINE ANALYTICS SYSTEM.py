import numpy as np
import matplotlib.pyplot as plt 

# ADVANCED FACTORY MACHINE ANALYTICS SYSTEM
class ScrewFactoryAnalytics:
    
    # INITIALIZE FACTORY CONFIGURATION
    def __init__( self , mean , std , count , upper , lower ):
        self.mean=mean
        self.std=std
        self.count=count
        self.upper=upper
        self.lower=lower
    
    # GENERATE MACHINE PRODUCTION DATA
    def generate_data(self):

        self.data = np.random.normal(
            loc=self.mean,
            scale=self.std,
            size=self.count
        )
        
    # QUALITY ANALYSIS
    def Analyze(self):

        #defective screws
        self.defects = self.data[(self.data<self.lower)|(self.data>self.upper)]
        self.defetc_count = len(self.defects)
        self.defects_percent = (self.defetc_count/self.count)*100

        # Basic statistics
        self.actual_mean = np.mean(self.data)
        self.actual_std = np.std(self.data)
        self.varience = np.var(self.data)

        # ---------------- REPORT ----------------
        print("\n")
        print("="*55)
        print("        FACTORY MACHINE ANALYTICS REPORT")
        print("="*55)

        print(f"Total Production    :{self.count}")
        print(f"Target Mean Length  :{self.mean:.4f} cm")
        print(f"actual Mean Length  :{self.actual_mean:.4f} cm")

        print(f"\n Stander Diviation :{self.actual_std:.4f}")
        print(f"Varience             :{self.varience:.6f}")

        print(f"\n Lower Tolerance   :{self.lower} cm")
        print(f"Upper Tolerance      :{self.upper} cm")

        print(F"\n Defective Screws  :{self.defetc_count}")
        print(f"Defective Percentage :{self.defects_percent:.2f}%")

        # Machine condition logic
        if self.defects_percent < 2:
            print("\n Machine Status     : excellent")
        elif self.defects_percent < 5:
            print("\n Machine Status     : Good")
        elif self.defects_percent < 10:
            print("\n Machine Status     : Warning")
        else:
            print("\n Machine Status     : Critical")

        # Maintenance alert
        if self.defects_percent > 10:
            print("Maintenance Alert     : Required")
        
        print("="*55)
    
    # VISUALIZATION SYSTEM
    def visualize(self):

        plt.figure(figsize=(14,7))

        #Histogram 
        counts,bins,patches=plt.hist(self.data,bins=80,density=True,edgecolor='black')

        # HIGHLIGHT DEFECT REGIONS
        # -------------------------------------------------

        for patch, left_edge in zip(patches, bins):

            if (
                left_edge < self.lower or
                left_edge > self.upper
            ):
                patch.set_facecolor('red')

        # -------------------------------------------------
        # MEAN LINE
        # -------------------------------------------------

        plt.axvline(
            self.actual_mean,
            linestyle='--',
            linewidth=3,
            label='Mean'
        )

        # -------------------------------------------------
        # TOLERANCE LIMITS
        # -------------------------------------------------

        plt.axvline(
            self.lower,
            linestyle='--',
            linewidth=3,
            label='Lower Tolerance'
        )

        plt.axvline(
            self.upper,
            linestyle='--',
            linewidth=3,
            label='Upper Tolerance'
        )

        # -------------------------------------------------
        # TITLES
        # -------------------------------------------------

        plt.title(
            "Factory Screw Length Distribution Analysis",
            fontsize=18
        )

        plt.xlabel(
            "Screw Length (cm)",
            fontsize=14
        )

        plt.ylabel(
            "Density",
            fontsize=14
        )

        # -------------------------------------------------
        # INFORMATION PANEL
        # -------------------------------------------------

        info_text = (
            f"Production : {self.count}\n"
            f"Mean       : {self.actual_mean:.4f}\n"
            f"Std Dev    : {self.actual_std:.4f}\n"
            f"Variance   : {self.varience:.6f}\n"
            f"Defects    : {self.defetc_count}\n"
            f"Defect %   : {self.defects_percent:.2f}%"
        )

        plt.text(
            0.02,
            0.95,
            info_text,
            transform=plt.gca().transAxes,
            fontsize=12,
            verticalalignment='top',
            bbox=dict(facecolor='white')
        )

        plt.legend()

        plt.grid(True)

        plt.show()

# =========================================================
# MAIN EXECUTION
# =========================================================

factory = ScrewFactoryAnalytics(

    mean=5,
    std=0.05,
    count=100000,
    lower=4.9,
    upper=5.1

)

# Generate production data
factory.generate_data()

# Analyze quality
factory.Analyze()

# Visualize analytics
factory.visualize()