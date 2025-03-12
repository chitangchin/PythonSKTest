class FinancialAIAgent:
    """
    An agent that provides financial recommendations and insights.
    """
    
    def __init__(self, message=None):
        self.name = "Financial AI Agent"
        self.message = message
    
    def get_recommendation(self, user_profile=None):
        """
        Get financial recommendations based on user profile.
        
        Args:
            user_profile: Optional user profile containing financial information
            
        Returns:
            A financial recommendation
        """
        # If a message was provided during initialization, use it for context
        if self.message:
            return f"Based on your message: '{self.message}', I recommend diversifying your investment portfolio."
        
        # Default recommendation
        return "Based on your profile, I recommend diversifying your investment portfolio."
    
    def analyze_financial_data(self, data):
        """
        Analyze financial data and provide insights.
        
        Args:
            data: Financial data to analyze
            
        Returns:
            Analysis results
        """
        try:
            if not data:
                return "Error: No financial data provided for analysis."
                
            # This is a placeholder implementation
            # In a real application, you would implement actual financial analysis logic here
            result = "Analysis complete. The data shows stable growth patterns."
            
            # Add more detailed analysis based on data type
            if isinstance(data, dict):
                if 'income' in data and 'expenses' in data:
                    savings_rate = (data['income'] - data['expenses']) / data['income'] * 100
                    result += f" Your savings rate is {savings_rate:.2f}%."
            
            return result
        except Exception as e:
            return f"Error analyzing financial data: {str(e)}"
