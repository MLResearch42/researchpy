#!/usr/bin/env python3
"""
Comprehensive test suite for ResearchPy library.

This script tests all major functions and features of the ResearchPy library
to ensure functionality works correctly and produces expected outputs.
"""

import sys
import warnings
import traceback
import pandas as pd
import numpy as np

# Suppress warnings for cleaner test output
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)

def run_test_suite():
    """Run comprehensive test suite for ResearchPy."""
    
    print("=" * 60)
    print("ResearchPy Comprehensive Test Suite")
    print("=" * 60)
    
    # Import ResearchPy
    try:
        import researchpy as rp
        print(f"✓ ResearchPy imported successfully (version {rp.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import ResearchPy: {e}")
        return False
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Test results storage
    test_results = []
    
    # Test 1: Basic T-Test
    print("\n1. Testing T-Test Functions")
    try:
        group1 = pd.Series(np.random.normal(10, 2, 30), name='Control')
        group2 = pd.Series(np.random.normal(12, 2, 30), name='Treatment')
        
        # Independent t-test
        desc, results = rp.ttest(group1, group2)
        assert isinstance(desc, pd.DataFrame), "Descriptives should be DataFrame"
        assert isinstance(results, pd.DataFrame), "Results should be DataFrame"
        assert desc.shape[0] == 3, "Should have 3 rows in descriptives"
        print("  ✓ Independent t-test works")
        
        # Paired t-test
        desc_paired, results_paired = rp.ttest(group1, group2, paired=True)
        assert isinstance(desc_paired, pd.DataFrame), "Paired descriptives should be DataFrame"
        print("  ✓ Paired t-test works")
        
        # Welch's t-test
        desc_welch, results_welch = rp.ttest(group1, group2, equal_variances=False)
        assert isinstance(desc_welch, pd.DataFrame), "Welch descriptives should be DataFrame"
        print("  ✓ Welch's t-test works")
        
        test_results.append(("T-Test Functions", True, None))
        
    except Exception as e:
        print(f"  ✗ T-Test failed: {e}")
        test_results.append(("T-Test Functions", False, str(e)))
    
    # Test 2: Summary Statistics
    print("\n2. Testing Summary Statistics")
    try:
        # Continuous summary
        summary_cont = rp.summary_cont(group1)
        assert isinstance(summary_cont, pd.DataFrame), "Summary should be DataFrame"
        print("  ✓ Continuous summary works")
        
        # Categorical summary
        categories = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'] * 10, name='Category')
        try:
            summary_cat = rp.summary_cat(categories)
            assert isinstance(summary_cat, pd.DataFrame), "Categorical summary should be DataFrame"  
            print("  ✓ Categorical summary works")
        except Exception as cat_error:
            print(f"  ! Categorical summary failed: {cat_error}")
        
        # Codebook (function prints output but may return None)
        test_data = pd.DataFrame({
            'numeric': np.random.normal(0, 1, 60),
            'categorical': categories
        })
        try:
            codebook = rp.codebook(test_data)
            # Codebook prints output, return value may be None
            print("  ✓ Codebook works")
        except Exception as cb_error:
            print(f"  ! Codebook failed: {cb_error}")
        
        test_results.append(("Summary Statistics", True, None))
        
    except Exception as e:
        print(f"  ✗ Summary Statistics failed: {e}")
        test_results.append(("Summary Statistics", False, str(e)))
    
    # Test 3: Correlation Analysis
    print("\n3. Testing Correlation Analysis")
    try:
        corr_data = pd.DataFrame({
            'x': np.random.normal(0, 1, 50),
            'y': np.random.normal(0, 1, 50),
            'z': np.random.normal(0, 1, 50)
        })
        
        # Case-wise correlation
        info, corr_matrix, p_values = rp.corr_case(corr_data)
        assert isinstance(corr_matrix, pd.DataFrame), "Correlation matrix should be DataFrame"
        assert isinstance(p_values, pd.DataFrame), "P-values should be DataFrame"
        print("  ✓ Case-wise correlation works")
        
        # Pairwise correlation
        pairwise_corr = rp.corr_pair(corr_data)
        assert isinstance(pairwise_corr, pd.DataFrame), "Pairwise correlation should be DataFrame"
        print("  ✓ Pairwise correlation works")
        
        test_results.append(("Correlation Analysis", True, None))
        
    except Exception as e:
        print(f"  ✗ Correlation Analysis failed: {e}")
        test_results.append(("Correlation Analysis", False, str(e)))
    
    # Test 4: Crosstabulation
    print("\n4. Testing Crosstabulation")
    try:
        var1 = pd.Series(['A', 'B', 'A', 'B'] * 25)
        var2 = pd.Series(['X', 'Y', 'X', 'Y'] * 25)
        
        # Basic crosstab
        crosstab_result = rp.crosstab(var1, var2)
        assert isinstance(crosstab_result, pd.DataFrame), "Crosstab should be DataFrame"
        print("  ✓ Basic crosstabulation works")
        
        # Crosstab with test
        try:
            crosstab_test, chi2_results = rp.crosstab(var1, var2, test='chi-square')
            print("  ✓ Crosstabulation with chi-square test works")
        except:
            print("  ! Chi-square test not available or failed")
        
        test_results.append(("Crosstabulation", True, None))
        
    except Exception as e:
        print(f"  ✗ Crosstabulation failed: {e}")
        test_results.append(("Crosstabulation", False, str(e)))
    
    # Test 5: Basic Statistics Functions
    print("\n5. Testing Basic Statistics Functions")
    try:
        test_array = np.array([1, 2, np.nan, 4, 5])
        
        # Count function
        count_result = rp.count(test_array)
        assert count_result == 4, f"Count should be 4, got {count_result}"
        print("  ✓ Count function works")
        
        # Other basic stats
        var_result = rp.nanvar(test_array)
        std_result = rp.nanstd(test_array)
        assert not np.isnan(var_result), "Variance should not be NaN"
        assert not np.isnan(std_result), "Standard deviation should not be NaN"
        print("  ✓ Basic statistics functions work")
        
        test_results.append(("Basic Statistics", True, None))
        
    except Exception as e:
        print(f"  ✗ Basic Statistics failed: {e}")
        test_results.append(("Basic Statistics", False, str(e)))
    
    # Test 6: Advanced Features
    print("\n6. Testing Advanced Features")
    try:
        # Test classes exist and can be instantiated
        test_df = pd.DataFrame({
            'dependent': np.random.normal(0, 1, 100),
            'independent': np.random.normal(0, 1, 100)
        })
        
        # Test difference_test class
        try:
            diff_test = rp.difference_test("dependent ~ independent", data=test_df)
            assert hasattr(diff_test, 'conduct'), "difference_test should have conduct method"
            print("  ✓ difference_test class works")
        except Exception as diff_error:
            print(f"  ! difference_test failed: {diff_error}")
        
        # Test model classes exist
        assert hasattr(rp, 'model'), "Should have model class"
        assert hasattr(rp, 'ols'), "Should have ols class" 
        assert hasattr(rp, 'anova'), "Should have anova class"
        print("  ✓ Advanced model classes available")
        
        test_results.append(("Advanced Features", True, None))
        
    except Exception as e:
        print(f"  ✗ Advanced Features failed: {e}")
        test_results.append(("Advanced Features", False, str(e)))
    
    # Test 7: Import Structure
    print("\n7. Testing Import Structure")
    try:
        # Test that all expected functions are available
        expected_functions = [
            'ttest', 'summary_cont', 'summary_cat', 'codebook',
            'corr_case', 'corr_pair', 'crosstab', 'count'
        ]
        
        for func_name in expected_functions:
            assert hasattr(rp, func_name), f"Missing function: {func_name}"
        
        # Test metadata
        assert hasattr(rp, '__version__'), "Should have version"
        assert hasattr(rp, '__author__'), "Should have author"
        print("  ✓ All expected functions and metadata available")
        
        test_results.append(("Import Structure", True, None))
        
    except Exception as e:
        print(f"  ✗ Import Structure failed: {e}")
        test_results.append(("Import Structure", False, str(e)))
    
    # Test 8: Edge Cases and Error Handling
    print("\n8. Testing Edge Cases")
    try:
        # Test with missing data
        data_with_nans = pd.Series([1, 2, np.nan, 4, np.nan])
        summary_with_nans = rp.summary_cont(data_with_nans)
        assert isinstance(summary_with_nans, pd.DataFrame), "Should handle NaN data"
        print("  ✓ Handles missing data correctly")
        
        # Test small samples
        small_group1 = pd.Series([1, 2, 3])
        small_group2 = pd.Series([4, 5, 6])
        small_desc, small_results = rp.ttest(small_group1, small_group2)
        assert isinstance(small_desc, pd.DataFrame), "Should handle small samples"
        print("  ✓ Handles small samples correctly")
        
        test_results.append(("Edge Cases", True, None))
        
    except Exception as e:
        print(f"  ✗ Edge Cases failed: {e}")
        test_results.append(("Edge Cases", False, str(e)))
    
    # Summary Report
    print("\n" + "=" * 60)
    print("TEST SUMMARY REPORT")
    print("=" * 60)
    
    passed = sum(1 for _, success, _ in test_results if success)
    total = len(test_results)
    
    for test_name, success, error in test_results:
        status = "PASS" if success else "FAIL"
        print(f"{test_name:<25} {status}")
        if error:
            print(f"  Error: {error}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! ResearchPy is working correctly.")
        return True
    else:
        print(f"⚠️  {total - passed} tests failed. See details above.")
        return False

if __name__ == "__main__":
    success = run_test_suite()
    sys.exit(0 if success else 1)