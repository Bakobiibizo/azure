    def create_context(self, user_message: Message,  context_window: Optional[int] = 8, primer_choice: Optional[int] = 0) -> List[Message]:
        primer = self.load_primer(primer_choice)
        history = self.load_history(context_window)
        self.context.append(primer)
        for all in history:
            self.context.append(all)
        self.context.append(user_message)
        return context