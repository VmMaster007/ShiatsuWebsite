function handleStickyNavbar() {
    const navbar = document.getElementById('navbar');
    const mainContent = document.getElementById('main-content-area');
    
    // Safety check
    if (!navbar || !mainContent) return;
    
    // Store the original offset top position when the page loads
    const stickyPoint = navbar.offsetTop; 
    
    // Store the original Bootstrap classes for easy removal/re-addition (the "reset")
    const originalClasses = ['mx-auto', 'mt-7', 'w-60']; 
    
    // The fixed classes we will add when scrolling
    const stickyClasses = ['fixed-top', 'w-100', 'shadow-sm']; 
    
    const handleScroll = () => {
        const scrollPosition = window.scrollY || document.documentElement.scrollTop;

        if (scrollPosition >= stickyPoint) {
            // --- SCROLL DOWN: Apply Sticky State ---
            
            // 1. Remove original positioning and add the sticky classes
            navbar.classList.remove(...originalClasses); 
            navbar.classList.add(...stickyClasses);

            // 2. INLINE STYLE FIX: Ensure it is flush with the top (removes the gap)
            navbar.style.top = '0px'; 
            navbar.style.margin = '0'; // Clear any residual margin
            
            // 3. FIX: Apply content margin to prevent jumping
            mainContent.style.marginTop = navbar.offsetHeight + 'px'; 

        } else {
            // --- SCROLL UP: Reset to Original State ---
            
            // 1. Remove the sticky classes
            navbar.classList.remove(...stickyClasses);
            
            // 2. Add the original positioning classes back for the "reset"
            navbar.classList.add(...originalClasses);
            
            // 3. INLINE STYLE RESET: Remove the sticky inline styles
            navbar.style.top = ''; // Reset to default CSS
            navbar.style.margin = ''; // Reset to default CSS

            // 4. FIX: Reset the content margin
            mainContent.style.marginTop = '0';
        }
    };
    
    window.addEventListener('scroll', handleScroll);
}

document.addEventListener('DOMContentLoaded', handleStickyNavbar);