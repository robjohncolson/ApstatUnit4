import os
import re
from pathlib import Path

def get_mapping():
    """Create a mapping of exact filenames to their new names."""
    return {
        # Progress Check PDFs
        "SG_Unit4ProgressCheckFRQ_67ebec98ca5609.67ebec9a0a4a34.63222075.pdf": "unit4_pc_frq_answers.pdf",
        "TB_Unit4ProgressCheckFRQ_67ebec94cf2817.67ebec95aa8628.28104681.pdf": "unit4_pc_frq_quiz.pdf",
        "SG_Unit4ProgressCheckMCQPartC_67ebec85aab150.67ebec8760b651.96130282.pdf": "unit4_pc_mcq_partc_quiz.pdf",
        "SG_Unit4ProgressCheckMCQPartB_67ebec7787d8e8.67ebec79dcfe85.61178077.pdf": "unit4_pc_mcq_partb_quiz.pdf",
        "SG_Unit4ProgressCheckMCQPartA_67ebec697983e8.67ebec6b1aae08.43518944.pdf": "unit4_pc_mcq_parta_quiz.pdf",
        
        # Topic 4.12
        "SG_TheGeometricDistributionQuiz_67ebec450e55d6.67ebec466c2e91.09211579.pdf": "4.12_answers.pdf",
        "TB_TheGeometricDistributionQuiz_67ebec41788d89.67ebec4296b4b8.27321610.pdf": "4.12_quiz.pdf",
        
        # Topic 4.11 (already renamed answer file exists)
        "TB_ParametersforaBinomialDistributionQuiz_67ebebf9eea900.67ebebfae52f25.48549811.pdf": "4.11_quiz.pdf",
        
        # Topic 4.10
        "SG_IntroductiontotheBinomialDistributionQuiz_67ebebc028ae01.67ebebc15a3276.55582334.pdf": "4.10_answers.pdf",
        "TB_IntroductiontotheBinomialDistributionQuiz_67ebebba9b2a79.67ebebbbc34de8.93765429.pdf": "4.10_quiz.pdf",
        
        # Topic 4.9 (already renamed answer file exists)
        "TB_CombiningRandomVariablesQuiz_67ebeb7dd3bff4.67ebeb7ed8cda9.65495827.pdf": "4.9_quiz.pdf",
        
        # Topic 4.8
        "SG_MeanandStandardDeviationofRandomVariablesQuiz_67ebeb3d904c41.67ebeb3ea5edb2.70217312.pdf": "4.8_answers.pdf",
        "TB_MeanandStandardDeviationofRandomVariablesQuiz_67ebeb39788161.67ebeb3a73a479.55949926.pdf": "4.8_quiz.pdf",
        
        # Topic 4.7
        "SG_IntroductiontoRandomVariablesandProbabilityDistributionsQuiz_67ebeb0b818857.67ebeb0c875812.44993092.pdf": "4.7_answers.pdf",
        "TB_IntroductiontoRandomVariablesandProbabilityDistributionsQuiz_67ebeb07a22130.67ebeb088d9e22.52768007.pdf": "4.7_quiz.pdf",
        
        # Topic 4.6
        "SG_IndependentEventsandUnionsofEventsQuiz_67ebeac16daf23.67ebeac2acdfd0.44197600.pdf": "4.6_answers.pdf",
        "TB_IndependentEventsandUnionsofEventsQuiz_67ebeabdd41ed5.67ebeabec9e320.32598324.pdf": "4.6_quiz.pdf",
        
        # Topic 4.5
        "SG_ConditionalProbabilityQuiz_67ebe9dfd03705.67ebe9e0d90e27.04984710.pdf": "4.5_answers.pdf",
        "TB_ConditionalProbabilityQuiz_67ebe9da6c2d06.67ebe9db5d2736.75152971.pdf": "4.5_quiz.pdf",
        
        # Topic 4.4 (already renamed answer file exists)
        "TB_MutuallyExclusiveEventsQuiz_67ebe991bff482.67ebe992b4a596.47423603.pdf": "4.4_quiz.pdf",
        
        # Topic 4.3
        "SG_IntroductiontoProbabilityQuiz_67ebe9423ddad9.67ebe943356281.63127532.pdf": "4.3_answers.pdf",
        "TB_IntroductiontoProbabilityQuiz_67ebe93e7afb93.67ebe93f66e623.02743692.pdf": "4.3_quiz.pdf",
        
        # Topic 4.2
        "SG_EstimatingProbabilitiesUsingSimulationQuiz_67ebe8d34f22a9.67ebe8d43f6c37.42361513.pdf": "4.2_answers.pdf",
        "TB_EstimatingProbabilitiesUsingSimulationQuiz_67ebe8ceaf2b34.67ebe8cf878608.34403051.pdf": "4.2_quiz.pdf"
    }

def rename_pdfs(source_dir):
    """Rename PDF files according to the mapping."""
    source_path = Path(source_dir)
    if not source_path.exists():
        print(f"Error: Directory {source_dir} does not exist")
        return

    # Get the mapping
    mapping = get_mapping()

    # Get list of PDF files in directory
    pdf_files = list(source_path.glob('*.pdf'))
    
    if not pdf_files:
        print(f"No PDF files found in {source_dir}")
        return

    print("\nFound PDF files:", *[f.name for f in pdf_files], sep='\n')
    print("\nMapping:", *[f"{k} -> {v}" for k, v in mapping.items()], sep='\n')

    # Rename files
    renamed_count = 0
    for pdf_file in pdf_files:
        if pdf_file.name in mapping:
            new_name = mapping[pdf_file.name]
            new_path = pdf_file.parent / new_name
            try:
                # Don't rename if the file already exists with the new name
                if not new_path.exists():
                    pdf_file.rename(new_path)
                    print(f"Renamed: {pdf_file.name} -> {new_name}")
                    renamed_count += 1
                else:
                    print(f"Skipped: {new_name} already exists")
            except Exception as e:
                print(f"Error renaming {pdf_file.name}: {str(e)}")
        else:
            print(f"Warning: No mapping found for {pdf_file.name}")

    print(f"\nRenamed {renamed_count} files")

def main():
    # Define the source directory
    source_dir = os.path.join('pdfs', 'unit4')
    
    # Perform the renaming
    rename_pdfs(source_dir)

if __name__ == '__main__':
    main()